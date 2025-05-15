# bakeshop/apps.py

from django.apps import AppConfig


class BakeshopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bakeshop'
    verbose_name = 'Bakeshop Management'
    
    def ready(self):
        """
        Import signals when the app is ready
        """
        import bakeshop.signals  # noqa