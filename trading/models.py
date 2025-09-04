from django.db import models

 
class SiteAsset(models.Model):
    key = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='site_assets/')

    def __str__(self):
        return self.key
    

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