from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.db import models

 
class SiteAsset(models.Model):
    key = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='site_assets/')

    def __str__(self):
        return self.key
    
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)
    

class AboutContent(models.Model):
    banner_image = models.ImageField(upload_to='about/banner/')
    banner_title = models.CharField(max_length=200, default="About TRACO")

    who_title = models.CharField(max_length=200, default="Who are We?")
    who_para1 = models.TextField(blank=True, null=True)
    who_para2 = models.TextField(blank=True, null=True)

    mission_title = models.CharField(max_length=200, default="Our Mission")
    mission_text = models.TextField(blank=True, null=True)
    mission_image = models.ImageField(upload_to='about/mission/', blank=True, null=True)

    vision_title = models.CharField(max_length=200, default="Our Vision")
    vision_text = models.TextField(blank=True, null=True)
    vision_image = models.ImageField(upload_to='about/vision/', blank=True, null=True)

    def _str_(self):
        return self.banner_title

class WhyChooseItem(models.Model):
    about = models.ForeignKey(AboutContent, related_name="why_items", on_delete=models.CASCADE)
    icon = models.ImageField(upload_to="about/why_icons/")
    title = models.CharField(max_length=200)

    def _str_(self):
        return self.title
