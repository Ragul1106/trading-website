import os
from django.core.management.base import BaseCommand
from django.core.files import File
from django.apps import apps
from django.conf import settings

class Command(BaseCommand):
    help = "Migrate local media files to Cloudinary"

    def handle(self, *args, **options):
        count = 0
        for model in apps.get_models():
            for field in model._meta.fields:
                if field.get_internal_type() in ["ImageField", "FileField"]:
                    qs = model.objects.exclude(**{f"{field.name}": ""}).exclude(**{f"{field.name}__isnull": True})
                    for obj in qs:
                        f = getattr(obj, field.name)
                        if f and not str(f).startswith("http"):
                            local_path = os.path.join(settings.MEDIA_ROOT, str(f))
                            if os.path.exists(local_path):
                                self.stdout.write(f"Uploading {local_path} for {model.__name__}({obj.pk})...")
                                with open(local_path, "rb") as fp:
                                    getattr(obj, field.name).save(os.path.basename(local_path), File(fp), save=True)
                                    count += 1
        self.stdout.write(self.style.SUCCESS(f"✅ Migration complete! {count} files uploaded to Cloudinary."))
