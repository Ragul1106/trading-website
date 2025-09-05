from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import SiteAsset
from .models import  WhyChooseItem, AboutContent, BlogHero
from .models import BlogTab, BlogPost
from django.contrib import admin
from .models import PartnerSection, PartnerLead, PartnerBenefitsSection, PartnerBenefit


admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "first_name", "email", "is_staff", "is_active")
    search_fields = ("username", "email")
    ordering = ("username",)


@admin.register(SiteAsset)
class SiteAssetAdmin(admin.ModelAdmin):
    list_display = ("key", "image")
    search_fields = ("key",)


class WhyChooseInline(admin.TabularInline):
    model = WhyChooseItem
    extra = 1


@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    list_display = ('banner_title', 'who_title')
    inlines = [WhyChooseInline]
    
    

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
   
   
   
   
@admin.register(PartnerLead)
class PartnerLeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "city", "is_verified", "created_at")
    search_fields = ("name", "email", "phone", "city")
    list_filter = ("is_verified", "created_at")

@admin.register(PartnerSection)
class PartnerSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "phone", "email")
    search_fields = ("heading", "phone", "email")

class PartnerBenefitInline(admin.TabularInline):
    model = PartnerBenefit
    extra = 0
    fields = ("order", "title", "description", "icon")
    ordering = ("order",)

@admin.register(PartnerBenefitsSection)
class PartnerBenefitsSectionAdmin(admin.ModelAdmin):
    list_display = ("heading_line1", "is_active")
    inlines = [PartnerBenefitInline]

    # Optional: allow only one section instance
    def has_add_permission(self, request):
        if PartnerBenefitsSection.objects.exists():
            return False
        return super().has_add_permission(request)
