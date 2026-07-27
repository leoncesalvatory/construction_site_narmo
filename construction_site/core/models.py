from django.db import models
from django.utils.text import slugify

class CompanyInfo(models.Model):
    # Existing fields...
    intro_text = models.TextField()
    years_experience = models.IntegerField(default=0)
    completed_projects = models.IntegerField(default=0)
    tagline = models.CharField(max_length=200, default="Building Strong Roads. Creating Lasting Structures.")
    mission = models.TextField(blank=True)
    vision = models.TextField(blank=True)
    core_values = models.TextField(blank=True)
    history = models.TextField(blank=True)

    # NEW: Add these
    logo = models.ImageField(upload_to='logo/', blank=True, null=True, 
                            help_text="Navbar logo: Transparent PNG, recommended 180-250px wide x 50-70px tall")
    hero_image = models.ImageField(upload_to='hero/', blank=True, null=True,
                                  help_text="Home page hero background: Wide landscape photo, at least 1920x1080px for full-screen sharpness")
    about_hero_image = models.ImageField(upload_to='hero/', blank=True, null=True,
                                        help_text="About page hero background - different from home")  # ← NEW

    class Meta:
        verbose_name_plural = "Company Info"  # Only one instance needed

class Certification(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='certifications/', blank=True)

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team/', blank=True)

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    benefits = models.TextField(blank=True)  # e.g., "Quality, Durability"
    image = models.ImageField(upload_to='services/')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('roads', 'Roads'),
        ('buildings', 'Buildings'),
        ('infrastructure', 'Infrastructure'),
    ]
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    year = models.CharField(max_length=50)  # e.g., "2023" or "Ongoing"
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    images = models.ManyToManyField('ProjectImage', blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class ProjectImage(models.Model):
    image = models.ImageField(upload_to='projects/')
    alt_text = models.CharField(max_length=200, blank=True)  # For SEO

class NewsPost(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class JobPosting(models.Model):
    title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    description = models.TextField()
    qualifications = models.TextField()
    instructions = models.TextField(blank=True)  # e.g., "Email resume to..."
    pdf = models.FileField(upload_to='jobs/', blank=True)  # Optional downloadable PDF

class ContactInfo(models.Model):
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField()
    working_hours = models.CharField(max_length=200)
    google_maps_embed = models.TextField(blank=True)  # Paste embed code from Google Maps
    whatsapp_number = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name_plural = "Contact Info"  # Only one instance

class CompanyLogo(models.Model):
    # ... existing fields ...
    logo = models.ImageField(upload_to='logo/', blank=True, null=True, help_text="Company logo for navbar (recommended size: 150x50 px, transparent PNG)")