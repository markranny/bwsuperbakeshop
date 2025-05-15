# dashboard/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count

from bakeshop.models import (
    SiteSettings, HomeSection, HomeBanner, 
    AboutSection, TeamMember, Award, Timeline,
    CareerSection, JobCategory, JobPosition, EmployeeTestimonial, Benefit,
    FranchiseSection, FranchiseModel, FranchiseeTestimonial, FAQ, InvestmentBreakdown, ProcessStep,
    StoreLocation, LocationStat,
    MenuCategory, MenuItem, FeaturedItem, SpecialOffer,
    ContactMessage, GalleryImage
)

from .forms import (
    SiteSettingsForm, HomeSectionForm, HomeBannerForm,
    AboutSectionForm, TeamMemberForm, AwardForm, TimelineForm,
    CareerSectionForm, JobCategoryForm, JobPositionForm, EmployeeTestimonialForm, BenefitForm,
    FranchiseSectionForm, FranchiseModelForm, FranchiseeTestimonialForm, FAQForm, InvestmentBreakdownForm,
    ProcessStepForm, StoreLocationForm, LocationStatForm,
    MenuCategoryForm, MenuItemForm, FeaturedItemForm, SpecialOfferForm,
    GalleryImageForm
)


# Dashboard Home
@login_required
def dashboard_home(request):
    """Dashboard home view with summary statistics"""
    # Get counts for various models
    stats = {
        'locations': StoreLocation.objects.count(),
        'menu_items': MenuItem.objects.count(),
        'jobs': JobPosition.objects.filter(is_active=True).count(),
        'messages': ContactMessage.objects.filter(is_read=False).count(),
    }
    
    # Recent contact messages
    recent_messages = ContactMessage.objects.order_by('-date_submitted')[:5]
    
    # Upcoming special offers
    special_offers = SpecialOffer.objects.filter(is_active=True).order_by('expiry_date')[:3]
    
    context = {
        'stats': stats,
        'recent_messages': recent_messages,
        'special_offers': special_offers,
        'active_page': 'dashboard',
    }
    return render(request, 'dashboard/index.html', context)


# Home Page Management
@login_required
def manage_home(request):
    """Manage home page content"""
    # Get all home page sections
    sections = HomeSection.objects.all().order_by('display_order')
    
    # Get all banners
    banners = HomeBanner.objects.all().order_by('display_order')
    
    context = {
        'sections': sections,
        'banners': banners,
        'active_page': 'home',
    }
    return render(request, 'dashboard/home.html', context)


@login_required
def home_section_edit(request, section_id):
    """Edit home page section"""
    section = get_object_or_404(HomeSection, id=section_id)
    
    if request.method == 'POST':
        form = HomeSectionForm(request.POST, request.FILES, instance=section)
        if form.is_valid():
            form.save()
            messages.success(request, f"The {section.get_section_type_display()} section has been updated successfully.")
            return redirect('dashboard:manage_home')
    else:
        form = HomeSectionForm(instance=section)
    
    context = {
        'form': form,
        'section': section,
        'active_page': 'home',
    }
    return render(request, 'dashboard/home_section_edit.html', context)


@login_required
def home_banner_add(request):
    """Add new home page banner"""
    if request.method == 'POST':
        form = HomeBannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New banner has been added successfully.")
            return redirect('dashboard:manage_home')
    else:
        form = HomeBannerForm()
    
    context = {
        'form': form,
        'active_page': 'home',
    }
    return render(request, 'dashboard/home_banner_form.html', context)


@login_required
def home_banner_edit(request, banner_id):
    """Edit home page banner"""
    banner = get_object_or_404(HomeBanner, id=banner_id)
    
    if request.method == 'POST':
        form = HomeBannerForm(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            form.save()
            messages.success(request, "Banner has been updated successfully.")
            return redirect('dashboard:manage_home')
    else:
        form = HomeBannerForm(instance=banner)
    
    context = {
        'form': form,
        'banner': banner,
        'active_page': 'home',
    }
    return render(request, 'dashboard/home_banner_form.html', context)


@login_required
def home_banner_delete(request, banner_id):
    """Delete home page banner"""
    banner = get_object_or_404(HomeBanner, id=banner_id)
    
    if request.method == 'POST':
        banner.delete()
        messages.success(request, "Banner has been deleted successfully.")
        return redirect('dashboard:manage_home')
    
    context = {
        'banner': banner,
        'active_page': 'home',
    }
    return render(request, 'dashboard/home_banner_delete.html', context)


# About Page Management
@login_required
def manage_about(request):
    """Manage about page content"""
    # Get all about page sections
    sections = AboutSection.objects.all()
    
    # Get team members
    team_members = TeamMember.objects.all().order_by('display_order')
    
    # Get awards
    awards = Award.objects.all().order_by('-year', 'display_order')
    
    # Get timeline events
    timeline_events = Timeline.objects.all().order_by('year')
    
    context = {
        'sections': sections,
        'team_members': team_members,
        'awards': awards,
        'timeline_events': timeline_events,
        'active_page': 'about',
    }
    return render(request, 'dashboard/about.html', context)


@login_required
def about_section_edit(request, section_id):
    """Edit about page section"""
    section = get_object_or_404(AboutSection, id=section_id)
    
    if request.method == 'POST':
        form = AboutSectionForm(request.POST, request.FILES, instance=section)
        if form.is_valid():
            form.save()
            messages.success(request, f"The {section.get_section_type_display()} section has been updated successfully.")
            return redirect('dashboard:manage_about')
    else:
        form = AboutSectionForm(instance=section)
    
    context = {
        'form': form,
        'section': section,
        'active_page': 'about',
    }
    return render(request, 'dashboard/about_section_edit.html', context)


@login_required
def team_member_add(request):
    """Add new team member"""
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New team member has been added successfully.")
            return redirect('dashboard:manage_about')
    else:
        form = TeamMemberForm()
    
    context = {
        'form': form,
        'active_page': 'about',
    }
    return render(request, 'dashboard/team_member_form.html', context)


@login_required
def team_member_edit(request, member_id):
    """Edit team member"""
    member = get_object_or_404(TeamMember, id=member_id)
    
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, "Team member has been updated successfully.")
            return redirect('dashboard:manage_about')
    else:
        form = TeamMemberForm(instance=member)
    
    context = {
        'form': form,
        'member': member,
        'active_page': 'about',
    }
    return render(request, 'dashboard/team_member_form.html', context)


@login_required
def team_member_delete(request, member_id):
    """Delete team member"""
    member = get_object_or_404(TeamMember, id=member_id)
    
    if request.method == 'POST':
        member.delete()
        messages.success(request, "Team member has been deleted successfully.")
        return redirect('dashboard:manage_about')
    
    context = {
        'member': member,
        'active_page': 'about',
    }
    return render(request, 'dashboard/team_member_delete.html', context)


@login_required
def award_add(request):
    """Add new award"""
    if request.method == 'POST':
        form = AwardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New award has been added successfully.")
            return redirect('dashboard:manage_about')
    else:
        form = AwardForm()
    
    context = {
        'form': form,
        'active_page': 'about',
    }
    return render(request, 'dashboard/award_form.html', context)


@login_required
def award_edit(request, award_id):
    """Edit award"""
    award = get_object_or_404(Award, id=award_id)
    
    if request.method == 'POST':
        form = AwardForm(request.POST, request.FILES, instance=award)
        if form.is_valid():
            form.save()
            messages.success(request, "Award has been updated successfully.")
            return redirect('dashboard:manage_about')
    else:
        form = AwardForm(instance=award)
    
    context = {
        'form': form,
        'award': award,
        'active_page': 'about',
    }
    return render(request, 'dashboard/award_form.html', context)


@login_required
def award_delete(request, award_id):
    """Delete award"""
    award = get_object_or_404(Award, id=award_id)
    
    if request.method == 'POST':
        award.delete()
        messages.success(request, "Award has been deleted successfully.")
        return redirect('dashboard:manage_about')
    
    context = {
        'award': award,
        'active_page': 'about',
    }
    return render(request, 'dashboard/award_delete.html', context)


@login_required
def timeline_add(request):
    """Add new timeline event"""
    if request.method == 'POST':
        form = TimelineForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New timeline event has been added successfully.")
            return redirect('dashboard:manage_about')
    else:
        form = TimelineForm()
    
    context = {
        'form': form,
        'active_page': 'about',
    }
    return render(request, 'dashboard/timeline_form.html', context)


@login_required
def timeline_edit(request, timeline_id):
    """Edit timeline event"""
    timeline = get_object_or_404(Timeline, id=timeline_id)
    
    if request.method == 'POST':
        form = TimelineForm(request.POST, instance=timeline)
        if form.is_valid():
            form.save()
            messages.success(request, "Timeline event has been updated successfully.")
            return redirect('dashboard:manage_about')
    else:
        form = TimelineForm(instance=timeline)
    
    context = {
        'form': form,
        'timeline': timeline,
        'active_page': 'about',
    }
    return render(request, 'dashboard/timeline_form.html', context)


@login_required
def timeline_delete(request, timeline_id):
    """Delete timeline event"""
    timeline = get_object_or_404(Timeline, id=timeline_id)
    
    if request.method == 'POST':
        timeline.delete()
        messages.success(request, "Timeline event has been deleted successfully.")
        return redirect('dashboard:manage_about')
    
    context = {
        'timeline': timeline,
        'active_page': 'about',
    }
    return render(request, 'dashboard/timeline_delete.html', context)


# Career Page Management
@login_required
def manage_career(request):
    """Manage career page content"""
    # Get all career page sections
    sections = CareerSection.objects.all()
    
    # Get job categories and positions
    categories = JobCategory.objects.annotate(position_count=Count('positions')).order_by('display_order')
    
    # Get all positions
    positions = JobPosition.objects.all().order_by('-is_active', '-is_featured', '-date_posted')
    
    # Get benefits
    benefits = Benefit.objects.all().order_by('display_order')
    
    # Get testimonials
    testimonials = EmployeeTestimonial.objects.all().order_by('display_order')
    
    # Get application process steps
    process_steps = ProcessStep.objects.filter(process_type='career').order_by('step_number')
    
    context = {
        'sections': sections,
        'categories': categories,
        'positions': positions,
        'benefits': benefits,
        'testimonials': testimonials,
        'process_steps': process_steps,
        'active_page': 'career',
    }
    return render(request, 'dashboard/career.html', context)


@login_required
def career_section_edit(request, section_id):
    """Edit career page section"""
    section = get_object_or_404(CareerSection, id=section_id)
    
    if request.method == 'POST':
        form = CareerSectionForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            messages.success(request, f"The {section.get_section_type_display()} section has been updated successfully.")
            return redirect('dashboard:manage_career')
    else:
        form = CareerSectionForm(instance=section)
    
    context = {
        'form': form,
        'section': section,
        'active_page': 'career',
    }
    return render(request, 'dashboard/career_section_edit.html', context)


@login_required
def job_category_add(request):
    """Add new job category"""
    if request.method == 'POST':
        form = JobCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New job category has been added successfully.")
            return redirect('dashboard:manage_career')
    else:
        form = JobCategoryForm()
    
    context = {
        'form': form,
        'active_page': 'career',
    }
    return render(request, 'dashboard/job_category_form.html', context)


@login_required
def job_category_edit(request, category_id):
    """Edit job category"""
    category = get_object_or_404(JobCategory, id=category_id)
    
    if request.method == 'POST':
        form = JobCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Job category has been updated successfully.")
            return redirect('dashboard:manage_career')
    else:
        form = JobCategoryForm(instance=category)
    
    context = {
        'form': form,
        'category': category,
        'active_page': 'career',
    }
    return render(request, 'dashboard/job_category_form.html', context)


@login_required
def job_category_delete(request, category_id):
    """Delete job category"""
    category = get_object_or_404(JobCategory, id=category_id)
    
    # Check if category has positions
    has_positions = category.positions.exists()
    
    if request.method == 'POST':
        if has_positions:
            messages.error(request, "Cannot delete category with existing positions.")
            return redirect('dashboard:manage_career')
        
        category.delete()
        messages.success(request, "Job category has been deleted successfully.")
        return redirect('dashboard:manage_career')
    
    context = {
        'category': category,
        'has_positions': has_positions,
        'active_page': 'career',
    }
    return render(request, 'dashboard/job_category_delete.html', context)


@login_required
def job_position_add(request):
    """Add new job position"""
    if request.method == 'POST':
        form = JobPositionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New job position has been added successfully.")
            return redirect('dashboard:manage_career')
    else:
        form = JobPositionForm()
    
    context = {
        'form': form,
        'active_page': 'career',
    }
    return render(request, 'dashboard/job_position_form.html', context)


@login_required
def job_position_edit(request, position_id):
    """Edit job position"""
    position = get_object_or_404(JobPosition, id=position_id)
    
    if request.method == 'POST':
        form = JobPositionForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
            messages.success(request, "Job position has been updated successfully.")
            return redirect('dashboard:manage_career')
    else:
        form = JobPositionForm(instance=position)
    
    context = {
        'form': form,
        'position': position,
        'active_page': 'career',
    }
    return render(request, 'dashboard/job_position_form.html', context)


@login_required
def job_position_delete(request, position_id):
    """Delete job position"""
    position = get_object_or_404(JobPosition, id=position_id)
    
    if request.method == 'POST':
        position.delete()
        messages.success(request, "Job position has been deleted successfully.")
        return redirect('dashboard:manage_career')
    
    context = {
        'position': position,
        'active_page': 'career',
    }
    return render(request, 'dashboard/job_position_delete.html', context)


@login_required
def employee_testimonial_add(request):
    """Add new employee testimonial"""
    if request.method == 'POST':
        form = EmployeeTestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New employee testimonial has been added successfully.")
            return redirect('dashboard:manage_career')
    else:
        form = EmployeeTestimonialForm()
    
    context = {
        'form': form,
        'active_page': 'career',
    }
    return render(request, 'dashboard/employee_testimonial_form.html', context)


@login_required
def employee_testimonial_edit(request, testimonial_id):
    """Edit employee testimonial"""
    testimonial = get_object_or_404(EmployeeTestimonial, id=testimonial_id)
    
    if request.method == 'POST':
        form = EmployeeTestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee testimonial has been updated successfully.")
            return redirect('dashboard:manage_career')
    else:
        form = EmployeeTestimonialForm(instance=testimonial)
    
    context = {
        'form': form,
        'testimonial': testimonial,
        'active_page': 'career',
    }
    return render(request, 'dashboard/employee_testimonial_form.html', context)


@login_required
def employee_testimonial_delete(request, testimonial_id):
    """Delete employee testimonial"""
    testimonial = get_object_or_404(EmployeeTestimonial, id=testimonial_id)
    
    if request.method == 'POST':
        testimonial.delete()
        messages.success(request, "Employee testimonial has been deleted successfully.")
        return redirect('dashboard:manage_career')
    
    context = {
        'testimonial': testimonial,
        'active_page': 'career',
    }
    return render(request, 'dashboard/employee_testimonial_delete.html', context)


@login_required
def benefit_add(request):
    """Add new benefit"""
    if request.method == 'POST':
        form = BenefitForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New benefit has been added successfully.")
            return redirect('dashboard:manage_career')
    else:
        form = BenefitForm()
    
    context = {
        'form': form,
        'active_page': 'career',
    }
    return render(request, 'dashboard/benefit_form.html', context)


@login_required
def benefit_edit(request, benefit_id):
    """Edit benefit"""
    benefit = get_object_or_404(Benefit, id=benefit_id)
    
    if request.method == 'POST':
        form = BenefitForm(request.POST, instance=benefit)
        if form.is_valid():
            form.save()
            messages.success(request, "Benefit has been updated successfully.")
            return redirect('dashboard:manage_career')
    else:
        form = BenefitForm(instance=benefit)
    
    context = {
        'form': form,
        'benefit': benefit,
        'active_page': 'career',
    }
    return render(request, 'dashboard/benefit_form.html', context)


@login_required
def benefit_delete(request, benefit_id):
    """Delete benefit"""
    benefit = get_object_or_404(Benefit, id=benefit_id)
    
    if request.method == 'POST':
        benefit.delete()
        messages.success(request, "Benefit has been deleted successfully.")
        return redirect('dashboard:manage_career')
    
    context = {
        'benefit': benefit,
        'active_page': 'career',
    }
    return render(request, 'dashboard/benefit_delete.html', context)

@login_required
def mark_message_as_read(request, message_id):
    """Mark message as read/unread"""
    message = get_object_or_404(ContactMessage, id=message_id)
    message.is_read = not message.is_read
    message.save()
    
    messages.success(request, f"Message marked as {'read' if message.is_read else 'unread'}.")
    return redirect('dashboard:contact_messages')


@login_required
def contact_message_delete(request, message_id):
    """Delete contact message"""
    message = get_object_or_404(ContactMessage, id=message_id)
    
    if request.method == 'POST':
        message.delete()
        messages.success(request, "Message has been deleted successfully.")
        return redirect('dashboard:contact_messages')
    
    context = {
        'message': message,
        'active_page': 'messages',
    }
    return render(request, 'dashboard/contact_message_delete.html', context)


# Site Settings
@login_required
def site_settings(request):
    """Manage site settings"""
    # Get or create site settings instance
    settings, created = SiteSettings.objects.get_or_create(id=1)
    
    if request.method == 'POST':
        form = SiteSettingsForm(request.POST, request.FILES, instance=settings)
        if form.is_valid():
            form.save()
            messages.success(request, "Site settings have been updated successfully.")
            return redirect('dashboard:site_settings')
    else:
        form = SiteSettingsForm(instance=settings)
    
    context = {
        'form': form,
        'settings': settings,
        'active_page': 'settings',
    }
    return render(request, 'dashboard/site_settings.html', context)