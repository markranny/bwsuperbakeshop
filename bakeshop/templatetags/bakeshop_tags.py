# bakeshop/templatetags/bakeshop_tags.py

from django import template
from django.utils.safestring import mark_safe
import re
import json

from bakeshop.models import MenuCategory, MenuItem, ContactMessage, JobPosition

register = template.Library()


@register.simple_tag
def active_link(request, view_name):
    """
    Returns 'active' if the current view matches the provided view_name,
    useful for navigation highlighting.
    
    Usage: {% active_link request 'bakeshop:index' %}
    """
    from django.urls import resolve, Resolver404
    try:
        if resolve(request.path_info).view_name == view_name:
            return 'active'
    except Resolver404:
        pass
    return ''


@register.filter
def to_json(value):
    """
    Converts a Python object to JSON string.
    
    Usage: {{ locations|to_json }}
    """
    return mark_safe(json.dumps(value))


@register.simple_tag
def unread_message_count():
    """
    Returns the count of unread messages.
    
    Usage: {% unread_message_count %}
    """
    return ContactMessage.objects.filter(is_read=False).count()


@register.simple_tag
def active_jobs_count():
    """
    Returns the count of active job positions.
    
    Usage: {% active_jobs_count %}
    """
    return JobPosition.objects.filter(is_active=True).count()


@register.inclusion_tag('bakeshop/tags/menu_categories.html')
def menu_categories():
    """
    Renders a list of active menu categories.
    
    Usage: {% menu_categories %}
    """
    categories = MenuCategory.objects.filter(is_active=True).order_by('display_order')
    return {'categories': categories}


@register.inclusion_tag('bakeshop/tags/featured_items.html')
def featured_items(count=3):
    """
    Renders featured menu items.
    
    Usage: {% featured_items 4 %}
    """
    items = MenuItem.objects.filter(is_active=True, is_bestseller=True).order_by('?')[:count]
    return {'items': items}


@register.filter
def phone_format(phone_number):
    """
    Formats a phone number.
    
    Usage: {{ contact.phone|phone_format }}
    """
    # Remove all non-numeric characters
    clean_number = re.sub(r'\D', '', str(phone_number))
    
    # Format based on length
    if len(clean_number) == 10:
        # US format: (555) 123-4567
        return f"({clean_number[:3]}) {clean_number[3:6]}-{clean_number[6:]}"
    elif len(clean_number) == 11 and clean_number[0] == '1':
        # US with country code: 1 (555) 123-4567
        return f"1 ({clean_number[1:4]}) {clean_number[4:7]}-{clean_number[7:]}"
    else:
        # Return as is if not matching standard formats
        return phone_number


@register.filter
def get_item(dictionary, key):
    """
    Returns the value for a key in a dictionary.
    
    Usage: {{ mydict|get_item:key_variable }}
    """
    if dictionary is None:
        return None
    return dictionary.get(key)


@register.filter
def truncate_chars(value, max_length):
    """
    Truncates a string to a specified length and appends ellipsis if truncated.
    
    Usage: {{ long_text|truncate_chars:100 }}
    """
    if len(value) <= max_length:
        return value
    
    truncated = value[:max_length]
    return truncated.rsplit(' ', 1)[0] + '...'


@register.simple_tag
def setting(name):
    """
    Returns a value from Django settings.
    
    Usage: {% setting 'SITE_NAME' %}
    """
    from django.conf import settings
    return getattr(settings, name, "")


@register.filter
def currency(value):
    """
    Formats a number as currency.
    
    Usage: {{ product.price|currency }}
    """
    try:
        value = float(value)
        return f"₱{value:,.2f}"
    except (ValueError, TypeError):
        return value


@register.filter
def hours_display(hours_text):
    """
    Formats business hours with proper HTML.
    
    Usage: {{ location.monday_hours|hours_display }}
    """
    if not hours_text:
        return "Closed"
    
    if hours_text.lower() == 'closed':
        return "<span class='text-danger'>Closed</span>"
    
    if hours_text.lower() == '24 hours' or hours_text.lower() == 'open 24 hours':
        return "<span class='text-success'>Open 24 Hours</span>"
    
    return hours_text


@register.filter
def location_status_badge(location):
    """
    Returns appropriate badge for location status.
    
    Usage: {{ location|location_status_badge }}
    """
    if not location.is_active:
        return "<span class='badge bg-danger'>Closed</span>"
    
    if location.is_coming_soon:
        return "<span class='badge bg-info'>Coming Soon</span>"
    
    if location.is_24hours:
        return "<span class='badge bg-success'>Open 24/7</span>"
    
    return "<span class='badge bg-primary'>Open</span>"


@register.filter
def job_badge(job):
    """
    Returns HTML for job badges based on job attributes.
    
    Usage: {{ job|job_badge }}
    """
    badges = []
    
    if job.is_urgent:
        badges.append("<span class='badge bg-danger'>Urgent</span>")
    
    if job.is_featured:
        badges.append("<span class='badge bg-success'>Featured</span>")
    
    if job.is_new or (job.date_posted and (job.date_posted.today() - job.date_posted).days <= 7):
        badges.append("<span class='badge bg-info'>New</span>")
    
    return mark_safe(' '.join(badges))


@register.filter
def menu_item_badges(item):
    """
    Returns HTML for menu item badges.
    
    Usage: {{ item|menu_item_badges }}
    """
    badges = []
    
    if item.is_bestseller:
        badges.append("<span class='badge bg-danger'>Bestseller</span>")
    
    if item.is_new:
        badges.append("<span class='badge bg-info'>New</span>")
    
    if item.is_seasonal:
        badges.append("<span class='badge bg-warning'>Seasonal</span>")
    
    if item.is_vegetarian:
        badges.append("<span class='badge bg-success'>Vegetarian</span>")
    
    if item.is_gluten_free:
        badges.append("<span class='badge bg-primary'>Gluten-Free</span>")
    
    if item.is_sugar_free:
        badges.append("<span class='badge bg-secondary'>Sugar-Free</span>")
    
    return mark_safe(' '.join(badges))


@register.inclusion_tag('bakeshop/tags/star_rating.html')
def star_rating(rating, max_rating=5):
    """
    Renders a star rating display.
    
    Usage: {% star_rating location.rating %}
    """
    if rating is None:
        rating = 0
        
    rating = float(rating)
    whole_stars = int(rating)
    half_star = rating - whole_stars >= 0.5
    empty_stars = max_rating - whole_stars - (1 if half_star else 0)
    
    return {
        'whole_stars': range(whole_stars),
        'half_star': half_star,
        'empty_stars': range(empty_stars)
    }