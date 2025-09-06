import os
import django
import cloudinary
import cloudinary.uploader

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trading_project.settings")
django.setup()

from django.conf import settings

# Initialize Cloudinary
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

# Path to your local media folder
media_path = os.path.join(settings.BASE_DIR, "media")

for root, dirs, files in os.walk(media_path):
    for file in files:
        file_path = os.path.join(root, file)

        # Fix folder path (Cloudinary requires '/')
        folder = os.path.relpath(root, media_path).replace("\\", "/")

        print(f"Uploading {file_path} to Cloudinary folder '{folder}'...")
        cloudinary.uploader.upload(file_path, folder=folder)
