# bakeshop/models.py

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

class BaseModel(models.Model):
    """Base model with common fields"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


# Site Settings
class SiteSettings(models.Model):
    """Global site settings"""
    site_name = models.CharField(max_length=100)
    site_tagline = models.CharField(max_length=200, blank=True)
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    favicon = models.ImageField(upload_to='site/', blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    footer_text = models.TextField(blank=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.site_name


# Home Page Models
class HomeSection(BaseModel):
    """Home page content sections"""
    SECTION_TYPES = (
        ('welcome', 'Welcome'),
        ('about', 'About Us'),
        ('menu', 'Menu'),
        ('testimonial', 'Testimonial'),
        ('newsletter', 'Newsletter'),
        ('featured', 'Featured Products'),
        ('promo', 'Promotion'),
    )
    
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200, blank=True)
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='home/sections/', blank=True, null=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"{self.get_section_type_display()}: {self.title}"


class HomeBanner(BaseModel):
    """Home page banner slides"""
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200, blank=True)
    image_desktop = models.ImageField(upload_to='home/banners/desktop/')
    image_mobile = models.ImageField(upload_to='home/banners/mobile/', blank=True, null=True)
    link_url = models.URLField(blank=True)
    button_text = models.CharField(max_length=50, blank=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title


# About Page Models
class AboutSection(BaseModel):
    """About page content sections"""
    SECTION_TYPES = (
        ('story', 'Our Story'),
        ('mission', 'Mission & Vision'),
        ('values', 'Core Values'),
        ('quality', 'Quality Commitment'),
        ('heritage', 'Heritage'),
    )
    
    title = models.CharField(max_length=100)
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='about/sections/', blank=True, null=True)

    def __str__(self):
        return f"{self.get_section_type_display()}: {self.title}"


class TeamMember(BaseModel):
    """Team members for about page"""
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='about/team/')
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"{self.name} - {self.position}"


class Award(BaseModel):
    """Awards and recognitions"""
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='about/awards/', blank=True, null=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-year', 'display_order']

    def __str__(self):
        return f"{self.title} ({self.year})"


class Timeline(models.Model):
    """Company history timeline events"""
    year = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        ordering = ['year']

    def __str__(self):
        return f"{self.year}: {self.title}"


# Career Page Models
class CareerSection(BaseModel):
    """Career page content sections"""
    SECTION_TYPES = (
        ('intro', 'Introduction'),
        ('culture', 'Company Culture'),
        ('benefits', 'Benefits'),
        ('growth', 'Career Growth'),
        ('process', 'Hiring Process'),
    )
    
    title = models.CharField(max_length=100)
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES)
    content = RichTextUploadingField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.get_section_type_display()}: {self.title}"


class JobCategory(BaseModel):
    """Job categories"""
    name = models.CharField(max_length=100)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Job Categories"
        ordering = ['display_order']

    def __str__(self):
        return self.name


class JobPosition(BaseModel):
    """Job openings"""
    EMPLOYMENT_TYPES = (
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('contract', 'Contract'),
        ('temporary', 'Temporary'),
        ('internship', 'Internship'),
    )
    
    title = models.CharField(max_length=100)
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE, related_name='positions')
    location = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPES)
    description = RichTextUploadingField()
    responsibilities = RichTextUploadingField()
    requirements = RichTextUploadingField()
    benefits = RichTextUploadingField(blank=True)
    salary_range = models.CharField(max_length=100, blank=True)
    application_email = models.EmailField()
    date_posted = models.DateField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    is_urgent = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-is_featured', '-date_posted']

    def __str__(self):
        return f"{self.title} ({self.get_employment_type_display()})"


class EmployeeTestimonial(BaseModel):
    """Employee testimonials"""
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    years_at_company = models.PositiveIntegerField()
    testimonial = models.TextField()
    image = models.ImageField(upload_to='career/testimonials/')
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"{self.name} - {self.position}"


class Benefit(models.Model):
    """Employee benefits"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Font Awesome class or icon name")
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title


# Franchise Page Models
class FranchiseSection(BaseModel):
    """Franchise page content sections"""
    SECTION_TYPES = (
        ('intro', 'Introduction'),
        ('why', 'Why Franchise With Us'),
        ('requirements', 'Requirements'),
        ('support', 'Support & Training'),
        ('process', 'Application Process'),
    )
    
    title = models.CharField(max_length=100)
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES)
    content = RichTextUploadingField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.get_section_type_display()}: {self.title}"


class FranchiseModel(BaseModel):
    """Franchise business models"""
    name = models.CharField(max_length=100)
    description = RichTextUploadingField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    space_required = models.CharField(max_length=100)
    features = models.TextField()
    is_recommended = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.name


class FranchiseeTestimonial(BaseModel):
    """Franchisee testimonials"""
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    years_as_franchisee = models.PositiveIntegerField()
    testimonial = models.TextField()
    image = models.ImageField(upload_to='franchise/testimonials/')
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"{self.name} - {self.location}"


class FAQ(models.Model):
    """Frequently asked questions"""
    CATEGORIES = (
        ('general', 'General'),
        ('franchise', 'Franchise'),
        ('menu', 'Menu & Products'),
        ('order', 'Ordering'),
    )
    
    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORIES)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['category', 'display_order']
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question


class InvestmentBreakdown(models.Model):
    """Franchise investment breakdown"""
    component = models.CharField(max_length=100)
    express_cost = models.DecimalField(max_digits=10, decimal_places=2)
    standard_cost = models.DecimalField(max_digits=10, decimal_places=2)
    premium_cost = models.DecimalField(max_digits=10, decimal_places=2)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.component


class ProcessStep(models.Model):
    """Steps for application processes (career, franchise)"""
    PROCESS_TYPES = (
        ('career', 'Career Application'),
        ('franchise', 'Franchise Application'),
    )
    
    process_type = models.CharField(max_length=20, choices=PROCESS_TYPES)
    step_number = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True, help_text="Font Awesome class or icon name")

    class Meta:
        ordering = ['process_type', 'step_number']

    def __str__(self):
        return f"{self.get_process_type_display()} - Step {self.step_number}: {self.title}"


# Location Page Models
class StoreLocation(BaseModel):
    """Store locations"""
    LOCATION_TYPES = (
        ('store', 'Retail Store'),
        ('express', 'Express Location'),
        ('cafe', 'Café & Dining'),
    )
    
    name = models.CharField(max_length=100)
    location_type = models.CharField(max_length=20, choices=LOCATION_TYPES)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='locations/')
    
    # Contact info
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    
    # Hours
    monday_hours = models.CharField(max_length=100, blank=True)
    tuesday_hours = models.CharField(max_length=100, blank=True)
    wednesday_hours = models.CharField(max_length=100, blank=True)
    thursday_hours = models.CharField(max_length=100, blank=True)
    friday_hours = models.CharField(max_length=100, blank=True)
    saturday_hours = models.CharField(max_length=100, blank=True)
    sunday_hours = models.CharField(max_length=100, blank=True)
    is_24hours = models.BooleanField(default=False)
    
    # Map
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    
    # Status
    is_featured = models.BooleanField(default=False)
    is_coming_soon = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    class Meta:
        ordering = ['city', 'name']

    def __str__(self):
        return f"{self.name} - {self.city}, {self.state}"


class LocationStat(models.Model):
    """Statistics for locations page"""
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"{self.label}: {self.value}"


# Menu Page Models
class MenuCategory(BaseModel):
    """Menu categories"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='menu/categories/', blank=True, null=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Menu Categories"
        ordering = ['display_order']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class MenuItem(BaseModel):
    """Menu items"""
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu/items/')
    
    # Dietary info
    is_vegetarian = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    is_sugar_free = models.BooleanField(default=False)
    
    # Status
    is_bestseller = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    is_seasonal = models.BooleanField(default=False)
    
    # Tags for searching/filtering
    tags = models.CharField(max_length=255, blank=True)
    
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['category__display_order', 'display_order']

    def __str__(self):
        return f"{self.name} - {self.category.name}"


class FeaturedItem(BaseModel):
    """Featured menu items for homepage"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu/featured/')
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title


class SpecialOffer(BaseModel):
    """Special offers and promotions"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu/offers/')
    discount_percentage = models.PositiveIntegerField(blank=True, null=True)
    expiry_date = models.DateField()

    class Meta:
        ordering = ['expiry_date']

    def __str__(self):
        return self.title


# Contact Page Models
class ContactMessage(models.Model):
    """Contact form submissions"""
    # Basic contact info
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    # Franchise inquiry
    is_franchise_inquiry = models.BooleanField(default=False)
    investment_level = models.CharField(max_length=50, blank=True)
    preferred_location = models.CharField(max_length=100, blank=True)
    
    # Job application
    is_job_application = models.BooleanField(default=False)
    position_applied = models.CharField(max_length=100, blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    
    # Status
    date_submitted = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-date_submitted']

    def __str__(self):
        return f"{self.name} - {self.subject}"


# Gallery
class GalleryImage(BaseModel):
    """Gallery images for various pages"""
    GALLERY_TYPES = (
        ('about', 'About Us'),
        ('menu', 'Menu & Products'),
        ('location', 'Locations'),
        ('career', 'Career'),
        ('franchise', 'Franchise'),
    )
    
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='gallery/')
    gallery_type = models.CharField(max_length=20, choices=GALLERY_TYPES)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['gallery_type', 'display_order']

    def __str__(self):
        return f"{self.title} - {self.get_gallery_type_display()}"