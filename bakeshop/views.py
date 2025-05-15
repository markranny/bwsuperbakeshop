# bakeshop/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import (
    SiteSettings, HomeSection, HomeBanner,
    AboutSection, TeamMember, Award, Timeline,
    CareerSection, JobCategory, JobPosition, EmployeeTestimonial, Benefit,
    FranchiseSection, FranchiseModel, FranchiseeTestimonial, FAQ, InvestmentBreakdown,
    StoreLocation, LocationStat, ProcessStep,
    MenuCategory, MenuItem, FeaturedItem, SpecialOffer,
    ContactMessage, GalleryImage
)
from .forms import ContactForm, JobApplicationForm, FranchiseInquiryForm


def index(request):
    """Homepage view"""
    # Get hero banners
    banners = HomeBanner.objects.filter(is_active=True).order_by('display_order')
    
    # Get home sections
    sections = {}
    for section in HomeSection.objects.filter(is_active=True).order_by('display_order'):
        sections[section.section_type] = section
    
    context = {
        'banners': banners,
        'sections': sections,
    }
    return render(request, 'bakeshop/index.html', context)


def about(request):
    """About us page view"""
    # Get about sections
    sections = {}
    for section in AboutSection.objects.filter(is_active=True):
        sections[section.section_type] = section
    
    # Get team members
    team_members = TeamMember.objects.filter(is_active=True).order_by('display_order')
    
    # Get awards
    awards = Award.objects.all().order_by('-year', 'display_order')
    
    # Get timeline events
    timeline_events = Timeline.objects.all().order_by('year')
    
    # Get gallery images
    gallery_images = GalleryImage.objects.filter(gallery_type='about', is_active=True).order_by('display_order')
    
    context = {
        'sections': sections,
        'team_members': team_members,
        'awards': awards,
        'timeline_events': timeline_events,
        'gallery_images': gallery_images,
    }
    return render(request, 'bakeshop/about.html', context)


def menu(request):
    """Menu page view"""
    # Get all menu categories
    categories = MenuCategory.objects.filter(is_active=True).order_by('display_order')
    
    # Get featured menu items
    featured_items = FeaturedItem.objects.filter(is_active=True).order_by('display_order')
    
    # Get current special offers
    special_offers = SpecialOffer.objects.filter(is_active=True)
    
    # Get all menu items or filter by category if specified
    category_slug = request.GET.get('category')
    
    if category_slug:
        category = get_object_or_404(MenuCategory, slug=category_slug)
        menu_items = MenuItem.objects.filter(category=category, is_active=True).order_by('display_order')
        current_category = category
    else:
        menu_items = MenuItem.objects.filter(is_active=True).order_by('category__display_order', 'display_order')
        current_category = None
    
    # Apply filters if any
    is_vegetarian = request.GET.get('vegetarian') == 'on'
    is_gluten_free = request.GET.get('gluten_free') == 'on'
    is_sugar_free = request.GET.get('sugar_free') == 'on'
    is_new = request.GET.get('new') == 'on'
    
    if is_vegetarian:
        menu_items = menu_items.filter(is_vegetarian=True)
    
    if is_gluten_free:
        menu_items = menu_items.filter(is_gluten_free=True)
    
    if is_sugar_free:
        menu_items = menu_items.filter(is_sugar_free=True)
    
    if is_new:
        menu_items = menu_items.filter(is_new=True)
    
    context = {
        'categories': categories,
        'menu_items': menu_items,
        'featured_items': featured_items,
        'special_offers': special_offers,
        'current_category': current_category,
        'filters': {
            'vegetarian': is_vegetarian,
            'gluten_free': is_gluten_free,
            'sugar_free': is_sugar_free,
            'new': is_new,
        }
    }
    return render(request, 'bakeshop/menu.html', context)


def menu_category(request, category_slug):
    """Menu category page view"""
    category = get_object_or_404(MenuCategory, slug=category_slug, is_active=True)
    menu_items = MenuItem.objects.filter(category=category, is_active=True).order_by('display_order')
    
    # Apply filters if any
    is_vegetarian = request.GET.get('vegetarian') == 'on'
    is_gluten_free = request.GET.get('gluten_free') == 'on'
    is_sugar_free = request.GET.get('sugar_free') == 'on'
    is_new = request.GET.get('new') == 'on'
    
    if is_vegetarian:
        menu_items = menu_items.filter(is_vegetarian=True)
    
    if is_gluten_free:
        menu_items = menu_items.filter(is_gluten_free=True)
    
    if is_sugar_free:
        menu_items = menu_items.filter(is_sugar_free=True)
    
    if is_new:
        menu_items = menu_items.filter(is_new=True)
    
    context = {
        'category': category,
        'menu_items': menu_items,
        'categories': MenuCategory.objects.filter(is_active=True).order_by('display_order'),
        'filters': {
            'vegetarian': is_vegetarian,
            'gluten_free': is_gluten_free,
            'sugar_free': is_sugar_free,
            'new': is_new,
        }
    }
    return render(request, 'bakeshop/menu_category.html', context)


def special_offers(request):
    """Special offers page view"""
    offers = SpecialOffer.objects.filter(is_active=True)
    
    context = {
        'offers': offers,
    }
    return render(request, 'bakeshop/special_offers.html', context)


def career(request):
    """Career page view"""
    # Get career sections
    sections = {}
    for section in CareerSection.objects.filter(is_active=True):
        sections[section.section_type] = section
    
    # Get job categories and positions
    categories = JobCategory.objects.all().order_by('display_order')
    
    # Get application process steps
    process_steps = ProcessStep.objects.filter(process_type='career').order_by('step_number')
    
    # Get benefits
    benefits = Benefit.objects.all().order_by('display_order')
    
    # Get testimonials
    testimonials = EmployeeTestimonial.objects.filter(is_active=True).order_by('display_order')
    
    # Get gallery images
    gallery_images = GalleryImage.objects.filter(gallery_type='career', is_active=True).order_by('display_order')
    
    context = {
        'sections': sections,
        'categories': categories,
        'process_steps': process_steps,
        'benefits': benefits,
        'testimonials': testimonials,
        'gallery_images': gallery_images,
    }
    return render(request, 'bakeshop/career.html', context)


def job_listings(request):
    """Job listings page view"""
    # Get all job categories
    categories = JobCategory.objects.all().order_by('display_order')
    
    # Filter jobs by category if specified
    category_id = request.GET.get('category')
    keyword = request.GET.get('keyword', '')
    
    if category_id:
        category = get_object_or_404(JobCategory, id=category_id)
        jobs = JobPosition.objects.filter(category=category, is_active=True)
    else:
        jobs = JobPosition.objects.filter(is_active=True)
    
    # Apply keyword search if specified
    if keyword:
        jobs = jobs.filter(
            Q(title__icontains=keyword) | 
            Q(description__icontains=keyword) | 
            Q(requirements__icontains=keyword) |
            Q(location__icontains=keyword)
        )
    
    # Paginate results
    paginator = Paginator(jobs.order_by('-is_featured', '-is_urgent', '-date_posted'), 10)
    page_number = request.GET.get('page')
    jobs_page = paginator.get_page(page_number)
    
    context = {
        'categories': categories,
        'jobs': jobs_page,
        'keyword': keyword,
        'selected_category': int(category_id) if category_id else None,
    }
    return render(request, 'bakeshop/job_listings.html', context)


def job_detail(request, job_id):
    """Job detail page view"""
    job = get_object_or_404(JobPosition, id=job_id, is_active=True)
    
    context = {
        'job': job,
    }
    return render(request, 'bakeshop/job_detail.html', context)


def job_apply(request, job_id):
    """Job application page view"""
    job = get_object_or_404(JobPosition, id=job_id, is_active=True)
    
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.is_job_application = True
            message.position_applied = job.title
            message.subject = f"Application for {job.title}"
            message.save()
            
            messages.success(request, "Your application has been submitted successfully!")
            return redirect('bakeshop:contact_thank_you')
    else:
        form = JobApplicationForm()
    
    context = {
        'job': job,
        'form': form,
    }
    return render(request, 'bakeshop/job_apply.html', context)


def franchise(request):
    """Franchise page view"""
    # Get franchise sections
    sections = {}
    for section in FranchiseSection.objects.filter(is_active=True):
        sections[section.section_type] = section
    
    # Get franchise models
    models = FranchiseModel.objects.all().order_by('display_order')
    
    # Get investment breakdown
    investment_items = InvestmentBreakdown.objects.all().order_by('display_order')
    
    # Get franchise process steps
    process_steps = ProcessStep.objects.filter(process_type='franchise').order_by('step_number')
    
    # Get FAQs
    faqs = FAQ.objects.filter(category='franchise').order_by('display_order')
    
    # Get testimonials
    testimonials = FranchiseeTestimonial.objects.filter(is_active=True).order_by('display_order')
    
    context = {
        'sections': sections,
        'models': models,
        'investment_items': investment_items,
        'process_steps': process_steps,
        'faqs': faqs,
        'testimonials': testimonials,
    }
    return render(request, 'bakeshop/franchise.html', context)


def franchise_request(request):
    """Franchise request form view"""
    if request.method == 'POST':
        form = FranchiseInquiryForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.is_franchise_inquiry = True
            message.subject = "Franchise Inquiry"
            message.save()
            
            messages.success(request, "Your franchise inquiry has been submitted successfully!")
            return redirect('bakeshop:contact_thank_you')
    else:
        form = FranchiseInquiryForm()
    
    context = {
        'form': form,
    }
    return render(request, 'bakeshop/franchise_request.html', context)


def location(request):
    """Locations page view"""
    # Get all store locations
    store_filter = request.GET.get('filter', 'all')
    
    if store_filter == 'all':
        locations = StoreLocation.objects.filter(is_active=True)
    else:
        locations = StoreLocation.objects.filter(location_type=store_filter, is_active=True)
    
    # Get featured location
    featured_location = StoreLocation.objects.filter(is_featured=True, is_active=True).first()
    
    # Get location statistics
    stats = LocationStat.objects.all().order_by('display_order')
    
    context = {
        'locations': locations,
        'featured_location': featured_location,
        'stats': stats,
        'current_filter': store_filter,
    }
    return render(request, 'bakeshop/location.html', context)


def location_detail(request, location_id):
    """Location detail page view"""
    location = get_object_or_404(StoreLocation, id=location_id, is_active=True)
    
    context = {
        'location': location,
    }
    return render(request, 'bakeshop/location_detail.html', context)


def location_search(request):
    """Location search view"""
    query = request.GET.get('query', '')
    radius = request.GET.get('radius', '10')
    
    # Basic search implementation (in a real app, you'd use geolocation)
    if query:
        locations = StoreLocation.objects.filter(
            Q(name__icontains=query) | 
            Q(address__icontains=query) | 
            Q(city__icontains=query) | 
            Q(state__icontains=query) | 
            Q(zip_code__icontains=query)
        ).filter(is_active=True)
    else:
        locations = StoreLocation.objects.filter(is_active=True)
    
    context = {
        'locations': locations,
        'query': query,
        'radius': radius,
    }
    return render(request, 'bakeshop/location_search.html', context)


def contact(request):
    """Contact page view"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('bakeshop:contact_thank_you')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'bakeshop/contact.html', context)


def contact_thank_you(request):
    """Thank you page after form submission"""
    return render(request, 'bakeshop/contact_thank_you.html')