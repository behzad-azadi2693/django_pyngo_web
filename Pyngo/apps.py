from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class PyngoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Pyngo'
    verbose_name = _('pyngo')
    verbose_name_plural = _('pyngo')