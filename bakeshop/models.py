# File: bakeshop/models.py

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

# Home Page Models
class Banner(BaseModel):
    ORIENTATION_CHOICES = (
        ('portrait', 'Portrait'),
        ('landscape', 'Landscape'),
    )
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='banners/')
    orientation = models.CharField(max_length=20, choices=ORIENTATION_CHOICES)
    url = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

# About Page Models
class AboutSection(BaseModel):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class TeamMember(BaseModel):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='team/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class Award(BaseModel):
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='awards/', blank=True, null=True)

    class Meta:
        ordering = ['-year']

    def __str__(self):
        return f"{self.title} ({self.year})"

# Menu Page Models
class MenuCategory(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='menu/categories/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Menu Categories'
        ordering = ['order']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class MenuItem(BaseModel):
    BADGE_CHOICES = (
        ('', 'None'),
        ('popular', 'Popular'),
        ('new', 'New'),
        ('seasonal', 'Seasonal'),
        ('bestseller', 'Bestseller'),
        ('limited', 'Limited Time'),
    )
    
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu/items/')
    is_vegetarian = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    is_sugar_free = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    badge = models.CharField(max_length=20, choices=BADGE_CHOICES, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['category', 'order']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class MenuItemTag(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='tags')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Location Page Models
class Location(BaseModel):
    LOCATION_TYPE_CHOICES = (
        ('store', 'Retail Store'),
        ('express', 'Express Location'),
        ('cafe', 'Café & Dining'),
    )
    
    name = models.CharField(max_length=100)
    location_type = models.CharField(max_length=20, choices=LOCATION_TYPE_CHOICES)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    hours_mon_fri = models.CharField(max_length=100, verbose_name="Monday-Friday Hours")
    hours_sat_sun = models.CharField(max_length=100, verbose_name="Saturday-Sunday Hours")
    is_open_24_7 = models.BooleanField(default=False)
    is_coming_soon = models.BooleanField(default=False)
    opening_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='locations/')
    description = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

# Career Page Models
class JobCategory(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name_plural = 'Job Categories'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class JobPosition(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE, related_name='positions')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='positions')
    employment_type = models.CharField(max_length=50, choices=[
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('contract', 'Contract'),
        ('temporary', 'Temporary'),
        ('internship', 'Internship'),
    ])
    salary_range = models.CharField(max_length=100, blank=True)
    description = RichTextUploadingField()
    responsibilities = RichTextUploadingField()
    requirements = RichTextUploadingField()
    benefits = RichTextUploadingField(blank=True)
    is_urgent = models.BooleanField(default=False)
    application_email = models.EmailField()
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class JobApplication(BaseModel):
    position = models.ForeignKey(JobPosition, on_delete=models.CASCADE, related_name='applications')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=[
        ('new', 'New'),
        ('reviewed', 'Reviewed'),
        ('interview', 'Interview'),
        ('hired', 'Hired'),
        ('rejected', 'Rejected'),
    ], default='new')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"

# Franchise Page Models
class FranchiseModel(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = RichTextUploadingField()
    investment = models.DecimalField(max_digits=10, decimal_places=2)
    space_required = models.CharField(max_length=100)
    recommended = models.BooleanField(default=False)
    image = models.ImageField(upload_to='franchise/models/')
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class FranchiseInvestmentDetail(models.Model):
    franchise_model = models.ForeignKey(FranchiseModel, on_delete=models.CASCADE, related_name='investment_details')
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.franchise_model.name} - {self.title}"

class FranchiseApplication(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    interested_model = models.ForeignKey(FranchiseModel, on_delete=models.SET_NULL, null=True, blank=True)
    investment_capacity = models.CharField(max_length=50, choices=[
        ('50k-100k', '$50,000 - $100,000'),
        ('100k-200k', '$100,000 - $200,000'),
        ('200k-300k', '$200,000 - $300,000'),
        ('300k+', 'More than $300,000'),
    ])
    business_experience = models.TextField()
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=[
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('meeting', 'Meeting Scheduled'),
        ('approved', 'Approved'),
        ('rejected', 'Not a Good Fit'),
    ], default='new')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.interested_model or 'General'}"

# Testimonials for various pages
class Testimonial(BaseModel):
    PAGE_CHOICES = (
        ('about', 'About Us'),
        ('franchise', 'Franchise'),
        ('career', 'Career'),
    )
    
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    quote = models.TextField()
    page = models.CharField(max_length=20, choices=PAGE_CHOICES)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['page', 'order']
    
    def __str__(self):
        return f"{self.name} - {self.get_page_display()}"

# Contact Form Submissions
class ContactSubmission(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"