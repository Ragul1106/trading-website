from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import SiteAsset, AboutContent, WhyChooseItem
from .models import BlogTab, BlogPost, BlogHero

admin.site.unregister(User)
class WhyChooseInline(admin.TabularInline):
    model = WhyChooseItem
    extra = 1

@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    list_display = ('banner_title', 'who_title')
    inlines = [WhyChooseInline]


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "first_name", "email", "is_staff", "is_active")
    search_fields = ("username", "email")
    ordering = ("username",)


@admin.register(BlogHero)
class BlogHeroAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle")

@admin.register(BlogTab)
class BlogTabAdmin(admin.ModelAdmin):
    list_display = ("tab_key",)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "date")
    list_filter = ("category",)
    search_fields = ("title", "short_desc")
    
