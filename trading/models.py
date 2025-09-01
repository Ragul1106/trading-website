from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.db import models

admin.site.unregister(User) 
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

class AboutContent(models.Model):
    banner_image = models.ImageField(upload_to='about/banner/')
    title = models.CharField(max_length=200)
    description = models.TextField()

    section1_image = models.ImageField(upload_to='about/section1/', blank=True, null=True)
    section1_text = models.TextField(blank=True, null=True)

    section2_image = models.ImageField(upload_to='about/section2/', blank=True, null=True)
    section2_text = models.TextField(blank=True, null=True)

 
    row_image_1 = models.ImageField(upload_to='about/row/', blank=True, null=True)
    row_image_2 = models.ImageField(upload_to='about/row/', blank=True, null=True)
    row_image_3 = models.ImageField(upload_to='about/row/', blank=True, null=True)
    row_image_4 = models.ImageField(upload_to='about/row/', blank=True, null=True)

    def __str__(self):
        return self.title