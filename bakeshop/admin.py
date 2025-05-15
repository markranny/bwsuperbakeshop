# bakeshop/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import (
    SiteSettings, HomeSection, HomeBanner, 
    AboutSection, TeamMember, Award, Timeline,
    CareerSection, JobCategory, JobPosition, EmployeeTestimonial, Benefit,
    FranchiseSection, FranchiseModel, FranchiseeTestimonial, FAQ, InvestmentBreakdown, ProcessStep,
    StoreLocation, LocationStat,
    MenuCategory, MenuItem, FeaturedItem, SpecialOffer,
    ContactMessage, GalleryImage
)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Site Identity', {
            'fields': ('site_name', 'site_tagline', 'logo', 'favicon')
        }),
        ('Contact Information', {
            'fields': ('phone_number', 'email', 'address')
        }),
        ('Social Media', {
            'fields': ('facebook_url', 'instagram_url', 'twitter_url')
        }),
        ('Footer', {
            'fields': ('footer_text',)
        }),
    )
    
    def has_add_permission(self, request):
        # Only allow one site settings instance
        return SiteSettings.objects.count() == 0


# Home Page Admin
@admin.register(HomeSection)
class HomeSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'section_type', 'display_order', 'is_active')
    list_filter = ('section_type', 'is_active')
    search_fields = ('title', 'content')
    list_editable = ('display_order', 'is_active')


@admin.register(HomeBanner)
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order', 'is_active', 'banner_preview')
    list_filter = ('is_active',)
    search_fields = ('title', 'subtitle')
    list_editable = ('display_order', 'is_active')
    
    def banner_preview(self, obj):
        if obj.image_desktop:
            return format_html('<img src="{}" height="50" />', obj.image_desktop.url)
        return "No Image"
    
    banner_preview.short_description = 'Banner Preview'


# About Page Admin
@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'section_type', 'is_active')
    list_filter = ('section_type', 'is_active')
    search_fields = ('title', 'content')
    list_editable = ('is_active',)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'display_order', 'is_active', 'image_preview')
    list_filter = ('is_active',)
    search_fields = ('name', 'position', 'bio')
    list_editable = ('display_order', 'is_active')
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50" />', obj.image.url)
        return "No Image"
    
    image_preview.short_description = 'Photo'


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'year', 'display_order')
    list_filter = ('year',)
    search_fields = ('title', 'organization', 'description')
    list_editable = ('display_order',)


@admin.register(Timeline)
class TimelineAdmin(admin.ModelAdmin):
    list_display = ('year', 'title')
    list_filter = ('year',)
    search_fields = ('year', 'title', 'description')
    ordering = ('year',)


# Career Page Admin
@admin.register(CareerSection)
class CareerSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'section_type', 'is_active')
    list_filter = ('section_type', 'is_active')
    search_fields = ('title', 'content')
    list_editable = ('is_active',)


class JobPositionInline(admin.TabularInline):
    model = JobPosition
    extra = 1
    fields = ('title', 'location', 'employment_type', 'is_active', 'is_featured', 'is_urgent')


@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_order', 'count_positions')
    list_editable = ('display_order',)
    inlines = [JobPositionInline]
    
    def count_positions(self, obj):
        return obj.positions.count()
    
    count_positions.short_description = 'Positions'


@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'employment_type', 'is_active', 'is_featured', 'is_urgent', 'date_posted')
    list_filter = ('category', 'employment_type', 'is_active', 'is_featured', 'is_urgent', 'date_posted')
    search_fields = ('title', 'location', 'description', 'requirements')
    list_editable = ('is_active', 'is_featured', 'is_urgent')
    date_hierarchy = 'date_posted'


@admin.register(EmployeeTestimonial)
class EmployeeTestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'years_at_company', 'display_order', 'is_active', 'image_preview')
    list_filter = ('is_active',)
    search_fields = ('name', 'position', 'testimonial')
    list_editable = ('display_order', 'is_active')
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50" />', obj.image.url)
        return "No Image"
    
    image_preview.short_description = 'Photo'


@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'display_order')
    search_fields = ('title', 'description')
    list_editable = ('display_order',)


# Franchise Page Admin
@admin.register(FranchiseSection)
class FranchiseSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'section_type', 'is_active')
    list_filter = ('section_type', 'is_active')
    search_fields = ('title', 'content')
    list_editable = ('is_active',)


@admin.register(FranchiseModel)
class FranchiseModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_recommended', 'display_order')
    list_filter = ('is_recommended',)
    search_fields = ('name', 'description', 'features')
    list_editable = ('is_recommended', 'display_order')


@admin.register(FranchiseeTestimonial)
class FranchiseeTestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'years_as_franchisee', 'display_order', 'is_active', 'image_preview')
    list_filter = ('is_active',)
    search_fields = ('name', 'location', 'testimonial')
    list_editable = ('display_order', 'is_active')
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50" />', obj.image.url)
        return "No Image"
    
    image_preview.short_description = 'Photo'


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'display_order')
    list_filter = ('category',)
    search_fields = ('question', 'answer')
    list_editable = ('display_order',)


@admin.register(InvestmentBreakdown)
class InvestmentBreakdownAdmin(admin.ModelAdmin):
    list_display = ('component', 'express_cost', 'standard_cost', 'premium_cost', 'display_order')
    search_fields = ('component',)
    list_editable = ('display_order',)


@admin.register(ProcessStep)
class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ('process_type', 'step_number', 'title')
    list_filter = ('process_type',)
    search_fields = ('title', 'description')
    list_editable = ('step_number',)


# Location Page Admin
@admin.register(StoreLocation)
class StoreLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location_type', 'city', 'state', 'is_featured', 'is_active', 'image_preview')
    list_filter = ('location_type', 'state', 'city', 'is_featured', 'is_active', 'is_24hours', 'is_coming_soon')
    search_fields = ('name', 'address', 'city', 'state', 'description')
    list_editable = ('is_featured', 'is_active')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'location_type', 'description', 'image')
        }),
        ('Address', {
            'fields': ('address', 'city', 'state', 'zip_code')
        }),
        ('Contact Information', {
            'fields': ('phone', 'email')
        }),
        ('Hours', {
            'fields': ('monday_hours', 'tuesday_hours', 'wednesday_hours', 'thursday_hours', 
                      'friday_hours', 'saturday_hours', 'sunday_hours', 'is_24hours')
        }),
        ('Map Location', {
            'fields': ('latitude', 'longitude')
        }),
        ('Status', {
            'fields': ('is_featured', 'is_coming_soon', 'is_active', 'rating')
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50" />', obj.image.url)
        return "No Image"
    
    image_preview.short_description = 'Photo'


@admin.register(LocationStat)
class LocationStatAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'display_order')
    list_editable = ('display_order',)


# Menu Page Admin
class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1
    fields = ('name', 'price', 'is_active', 'is_bestseller', 'is_new', 'display_order')


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_order', 'is_active', 'count_items')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
    list_editable = ('display_order', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [MenuItemInline]
    
    def count_items(self, obj):
        return obj.items.count()
    
    count_items.short_description = 'Items'


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'display_order', 'is_active', 'is_bestseller', 'is_new', 'image_preview')
    list_filter = ('category', 'is_active', 'is_bestseller', 'is_new', 'is_seasonal', 
                  'is_vegetarian', 'is_gluten_free', 'is_sugar_free')
    search_fields = ('name', 'description', 'tags')
    list_editable = ('display_order', 'is_active', 'is_bestseller', 'is_new')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'description', 'price', 'image')
        }),
        ('Dietary Information', {
            'fields': ('is_vegetarian', 'is_gluten_free', 'is_sugar_free')
        }),
        ('Status', {
            'fields': ('is_bestseller', 'is_new', 'is_seasonal', 'is_active')
        }),
        ('Additional Information', {
            'fields': ('tags', 'display_order')
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50" />', obj.image.url)
        return "No Image"
    
    image_preview.short_description = 'Photo'


@admin.register(FeaturedItem)
class FeaturedItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'display_order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    list_editable = ('display_order', 'is_active')


@admin.register(SpecialOffer)
class SpecialOfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'discount_percentage', 'expiry_date', 'is_active')
    list_filter = ('is_active', 'expiry_date')
    search_fields = ('title', 'description')
    list_editable = ('is_active',)


# Contact Messages
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date_submitted', 'is_read', 'message_type')
    list_filter = ('is_read', 'is_franchise_inquiry', 'is_job_application', 'date_submitted')
    search_fields = ('name', 'email', 'subject', 'message', 'position_applied', 'preferred_location')
    date_hierarchy = 'date_submitted'
    readonly_fields = ('date_submitted',)
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone', 'date_submitted')
        }),
        ('Message Details', {
            'fields': ('subject', 'message', 'is_read')
        }),
        ('Franchise Information', {
            'fields': ('is_franchise_inquiry', 'investment_level', 'preferred_location'),
            'classes': ('collapse',),
        }),
        ('Job Application', {
            'fields': ('is_job_application', 'position_applied', 'resume'),
            'classes': ('collapse',),
        }),
        ('Internal Notes', {
            'fields': ('notes',),
        }),
    )
    
    def message_type(self, obj):
        if obj.is_franchise_inquiry:
            return "Franchise Inquiry"
        elif obj.is_job_application:
            return "Job Application"
        return "General Contact"
    
    message_type.short_description = 'Type'


# Gallery Images
@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'gallery_type', 'display_order', 'is_active', 'image_preview')
    list_filter = ('gallery_type', 'is_active')
    search_fields = ('title', 'description')
    list_editable = ('display_order', 'is_active')
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50" />', obj.image.url)
        return "No Image"
    
    image_preview.short_description = 'Image'