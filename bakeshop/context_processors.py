# bakeshop/context_processors.py

from .models import SiteSettings

def global_settings(request):
    """
    Adds site settings to the context of all templates.
    """
    try:
        settings = SiteSettings.objects.get(id=1)
    except SiteSettings.DoesNotExist:
        # Create default settings if they don't exist
        settings = SiteSettings.objects.create(
            site_name="ELJIN SUPERBAKESHOP",
            site_tagline="Crafting Moments, Baking Memories"
        )
    
    return {
        'site_settings': settings
    }