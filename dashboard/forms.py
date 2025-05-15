# dashboard/forms.py

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from bakeshop.models import (
    SiteSettings, HomeSection, HomeBanner, 
    AboutSection, TeamMember, Award, Timeline,
    CareerSection, JobCategory, JobPosition, EmployeeTestimonial, Benefit,
    FranchiseSection, FranchiseModel, FranchiseeTestimonial, FAQ, InvestmentBreakdown, ProcessStep,
    StoreLocation, LocationStat,
    MenuCategory, MenuItem, FeaturedItem, SpecialOffer,
    GalleryImage
)


class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = '__all__'
        widgets = {
            'site_name': forms.TextInput(attrs={'class': 'form-control'}),
            'site_tagline': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.URLInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control'}),
            'footer_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


# Home Page Forms
class HomeSectionForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = HomeSection
        fields = ('title', 'subtitle', 'section_type', 'content', 'image', 'display_order', 'is_active')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'section_type': forms.Select(attrs={'class': 'form-select'}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class HomeBannerForm(forms.ModelForm):
    class Meta:
        model = HomeBanner
        fields = ('title', 'subtitle', 'image_desktop', 'image_mobile', 'link_url', 'button_text', 'display_order', 'is_active')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'link_url': forms.URLInput(attrs={'class': 'form-control'}),
            'button_text': forms.TextInput(attrs={'class': 'form-control'}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


# About Page Forms
class AboutSectionForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = AboutSection
        fields = ('title', 'section_type', 'content', 'image', 'is_active')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'section_type': forms.Select(attrs={'class': 'form-select'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ('name', 'position', 'bio', 'image', 'display_order', 'is_active')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = ('title', 'organization', 'year', 'description', 'image', 'display_order', 'is_active')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'organization': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class TimelineForm(forms.ModelForm):
    class Meta:
        model = Timeline
        fields = ('year', 'title', 'description')
        widgets = {
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


# Career Page Forms
class CareerSectionForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = CareerSection
        fields = ('title', 'section_type', 'content', 'is_active')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'section_type': forms.Select(attrs={'class': 'form-select'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class JobCategoryForm(forms.ModelForm):
    class Meta:
        model = JobCategory
        fields = ('name', 'display_order', 'is_active')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class JobPositionForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    responsibilities = forms.CharField(widget=CKEditorUploadingWidget())
    requirements = forms.CharField(widget=CKEditorUploadingWidget())
    benefits = forms.CharField(widget=CKEditorUploadingWidget(), required=False)
    
    class Meta:
        model = JobPosition
        fields = ('title', 'category', 'location', 'employment_type', 
                  'description', 'responsibilities', 'requirements', 'benefits',
                  'salary_range', 'application_email', 'is_featured', 'is_urgent', 'is_active', 'display_order')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'employment_type': forms.Select(attrs={'class': 'form-select'}),
            'salary_range': forms.TextInput(attrs={'class': 'form-control'}),
            'application_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_urgent': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class EmployeeTestimonialForm(forms.ModelForm):
    class Meta:
        model = EmployeeTestimonial
        fields = ('name', 'position', 'years_at_company', 'testimonial', 'image', 'display_order', 'is_active')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'years_at_company': forms.NumberInput(attrs={'class': 'form-control'}),
            'testimonial': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class BenefitForm(forms.ModelForm):
    class Meta:
        model = Benefit
        fields = ('title', 'description', 'icon', 'display_order')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'icon': forms.TextInput(attrs={'class': 'form-control'}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
        }


# Franchise Page Forms
class FranchiseSectionForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = FranchiseSection
        fields = ('title', 'section_type', 'content', 'is_active')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'section_type': forms.Select(attrs={'class': 'form-select'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class FranchiseModelForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = FranchiseModel
        fields = ('name', 'description', 'price', 'space_required', 'features', 'is_recommended', 'display_order', 'is_active')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'space_required': forms.TextInput(attrs={'class': 'form-control'}),
            'features': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'is_recommended': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class FranchiseeTestimonialForm(forms.ModelForm):
    class Meta:
        model = FranchiseeTestimonial
        fields = ('name', 'location', 'years_as_franchisee', 'testimonial', 'image', 'display_order', 'is_active')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'years_as_franchisee': forms.NumberInput(attrs={'class': 'form-control'}),
            'testimonial': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ('question', 'answer', 'category', 'display_order')
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control'}),
            'answer': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class InvestmentBreakdownForm(forms.ModelForm):
    class Meta:
        model = InvestmentBreakdown
        fields = ('component', 'express_cost', 'standard_cost', 'premium_cost', 'display_order')
        widgets = {
            'component': forms.TextInput(attrs={'class': 'form-control'}),
            'express_cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'standard_cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'premium_cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ProcessStepForm(forms.ModelForm):
    class Meta:
        model = ProcessStep
        fields = ('process_type', 'step_number', 'title', 'description', 'icon')
        widgets = {
            'process_type': forms.Select(attrs={'class': 'form-select'}),
            'step_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'icon': forms.TextInput(attrs={'class': 'form-control'}),
        }


# Location Forms
class StoreLocationForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(), required=False)
    
    class Meta:
        model = StoreLocation
        fields = ('name', 'location_type', 'description', 'image', 
                  'address', 'city', 'state', 'zip_code',
                  'phone', 'email',
                  'monday_hours', 'tuesday_hours', 'wednesday_hours', 'thursday_hours', 
                  'friday_hours', 'saturday_hours', 'sunday_hours', 'is_24hours',
                  'latitude', 'longitude',
                  'is_featured', 'is_coming_soon', 'is_active', 'rating')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location_type': forms.Select(attrs={'class': 'form-select'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'monday_hours': forms.TextInput(attrs={'class': 'form-control'}),
            'tuesday_hours': forms.TextInput(attrs={'class': 'form-control'}),
            'wednesday_hours': forms.TextInput(attrs={'class': 'form-control'}),
            'thursday_hours': forms.TextInput(attrs={'class': 'form-control'}),
            'friday_hours': forms.TextInput(attrs={'class': 'form-control'}),
            'saturday_hours': forms.TextInput(attrs={'class': 'form-control'}),
            'sunday_hours': forms.TextInput(attrs={'class': 'form-control'}),
            'is_24hours': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_coming_soon': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class LocationStatForm(forms.ModelForm):
    class Meta:
        model = LocationStat
        fields = ('label', 'value', 'display_order')
        widgets = {
            'label': forms.TextInput(attrs={'class': 'form-control'}),
            'value': forms.TextInput(attrs={'class': 'form-control'}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
        }


# Menu Forms
class MenuCategoryForm(forms.ModelForm):
    class Meta:
        model = MenuCategory
        fields = ('name', 'description', 'image', 'display_order', 'is_active')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ('name', 'category', 'description', 'price', 'image',
                  'is_vegetarian', 'is_gluten_free', 'is_sugar_free',
                  'is_bestseller', 'is_new', 'is_seasonal', 'is_active',
                  'tags', 'display_order')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_vegetarian': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_gluten_free': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_sugar_free': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_bestseller': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_new': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_seasonal': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class FeaturedItemForm(forms.ModelForm):
    class Meta:
        model = FeaturedItem
        fields = ('title', 'description', 'price', 'image', 'display_order', 'is_active')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class SpecialOfferForm(forms.ModelForm):
    class Meta:
        model = SpecialOffer
        fields = ('title', 'description', 'image', 'discount_percentage', 'expiry_date', 'is_active')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'discount_percentage': forms.NumberInput(attrs={'class': 'form-control'}),
            'expiry_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


# Gallery Image Form
class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ('title', 'description', 'image', 'gallery_type', 'display_order', 'is_active')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'gallery_type': forms.Select(attrs={'class': 'form-select'}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }