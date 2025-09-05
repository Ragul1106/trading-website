from django.core.management.base import BaseCommand
from trading.models import BlogPost
from django.conf import settings
import cloudinary.uploader
import os

class Command(BaseCommand):
    help = "Migrate BlogPost ImageFields to Cloudinary"

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show which files would be uploaded without actually uploading'
        )

    def handle(self, *args, **options):
        dry_run = options['dry_run']
        uploaded = 0
        skipped = 0

        for obj in BlogPost.objects.all():
            image = obj.image
            if not image:
                skipped += 1
                continue

            file_url = str(image)
            file_path = os.path.join(settings.MEDIA_ROOT, file_url)  # ALWAYS use MEDIA_ROOT

            print(f"DEBUG: {obj.pk} → file_url={file_url}, file_path={file_path}")

            # Skip if already a Cloudinary URL
            if file_url.startswith("http"):
                print(f"⏭️ Skipping remote file: {file_url}")
                skipped += 1
                continue

            if os.path.exists(file_path):
                if dry_run:
                    print(f"⏳ Would upload: {file_path}")
                    uploaded += 1
                else:
                    print(f"⏫ Uploading: {file_path} ...")
                    result = cloudinary.uploader.upload(
                        file_path,
                        folder="trading/blog_post_images"
                    )
                    obj.image = result["secure_url"]
                    obj.save(update_fields=["image"])
                    uploaded += 1
            else:
                print(f"⚠️ Missing file: {file_path}")
                skipped += 1

        self.stdout.write(self.style.SUCCESS(
            f"🎉 Migration complete! {uploaded} files uploaded, {skipped} skipped."
        ))
