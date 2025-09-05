from django.db import models


class SiteAsset(models.Model):
    key = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to="site_assets/")

    def __str__(self):
        return self.key


class AboutContent(models.Model):
    banner_image = models.ImageField(upload_to='about/banner/')
    banner_title = models.CharField(max_length=200, default="About TRACO")

    who_title = models.CharField(max_length=200, default="Who are We?")
    who_para1 = models.TextField(blank=True, null=True)
    who_para2 = models.TextField(blank=True, null=True)

    # Mission Section
    mission_title = models.CharField(max_length=200, default="Our Mission")
    mission_text = models.TextField(blank=True, null=True)
    mission_image = models.ImageField(upload_to='about/mission/', blank=True, null=True)

    # Vision Section
    vision_title = models.CharField(max_length=200, default="Our Vision")
    vision_text = models.TextField(blank=True, null=True)
    vision_image = models.ImageField(upload_to='about/vision/', blank=True, null=True)
    
    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"
        
    def _str_(self):
        return self.banner_title


class WhyChooseItem(models.Model):
    about = models.ForeignKey(AboutContent, related_name="why_items", on_delete=models.CASCADE)
    icon = models.ImageField(upload_to="about/why_icons/")
    title = models.CharField(max_length=200)
    def _str_(self):
        return self.title

class BlogHero(models.Model):
    title = models.CharField(max_length=200, default="Don’t Just Gain info")
    subtitle = models.CharField(max_length=200, default="Build Knowledge")
    description = models.TextField(
        default="Whether you’re a new investor or a market expert, we’ve got something for everyone at the TRACO blog"
    )
    image = models.ImageField(upload_to="blog/", blank=True, null=True)  
    sparkle = models.ImageField(upload_to="blog/", blank=True, null=True)  
    
    class Meta:
        verbose_name = "Blog Hero_Section"
        verbose_name_plural = "Blog Hero_Section"

    def __str__(self):
        return self.title

class BlogTab(models.Model):
    TAB_CHOICES = [
        ("stocks", "Stocks"),
        ("mutual", "Mutual Funds"),
        ("finance", "Personal Finance"),
        ("futures", "Futures & Options"),
    ]
    tab_key = models.CharField(max_length=20, choices=TAB_CHOICES, unique=True)

    class Meta:
        verbose_name = "Blog tabs"
        verbose_name_plural = "Blog tabs"
    def __str__(self):
        return self.get_tab_key_display()


class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ("stocks", "Stocks"),
        ("mutual", "Mutual Funds"),
        ("finance", "Personal Finance"),
        ("futures", "Futures & Options"),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    short_desc = models.TextField()
    read_time = models.CharField(max_length=50, default="5 Mins Read")
    date = models.DateField()
    image = models.ImageField(upload_to="blog_posts/", blank=True, null=True)

    class Meta:
        verbose_name = "Blog Posts"
        verbose_name_plural = "Blog Posts"
    def __str__(self):
        return self.title

class PartnerLead(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=80, blank=True)
    pincode = models.CharField(max_length=12, blank=True)
    otp = models.CharField(max_length=6, blank=True)        
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Partner Lead"
        verbose_name_plural = "Partner Leads"

    def __str__(self):
        return f"{self.name} ({self.email})"


class PartnerSection(models.Model):
    heading = models.CharField(
        max_length=200,
        default="Welcome to the First Step of Becoming a TRACO Partner"
    )
    sub_text = models.TextField(
        blank=True,
        null=True,
        default="Contact us Alternatively, You can Contact Our Business Partner Team"
    )
    phone = models.CharField(
        max_length=30,
        default="022 982231",
        help_text="Display phone number shown on the partner page"
    )
    email = models.EmailField(
        default="businesspartner@tranco.in",
        help_text="Display email shown on the partner page"
    )
    image = models.ImageField(
        upload_to="partner/",
        blank=True,
        null=True,
        help_text="Hero/side image for the partner page"
    )

    class Meta:
        verbose_name = "Partner Page Content"
        verbose_name_plural = "Partner Page Content"

    def __str__(self):
        return self.heading


class PartnerBenefitsSection(models.Model):
    # Big heading lines above the cards
    heading_line1 = models.CharField(
        max_length=200,
        default="People become partners to earn passive income and grow with a trusted brand."
    )
    heading_line2 = models.CharField(
        max_length=200,
        default="They get access to high commissions, marketing support, and long-term business potential."
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Partner – Benefits (Section 2)"
        verbose_name_plural = "Partner – Benefits (Section 2)"

    def __str__(self):
        return "Partner – Benefits Section"

class PartnerBenefit(models.Model):
    section = models.ForeignKey(
        PartnerBenefitsSection,
        related_name="items",
        on_delete=models.CASCADE
    )
    # Small card content
    title = models.CharField(max_length=120)
    description = models.TextField()
    icon = models.ImageField(upload_to="partner/benefit_icons/", blank=True, null=True)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order"]
        verbose_name = "Partner Benefit Item"
        verbose_name_plural = "Partner Benefit Items"

    def __str__(self):
        return f"{self.order}. {self.title}"
