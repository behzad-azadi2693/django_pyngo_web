from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('your name'))
    phone_regex = RegexValidator(regex=r'^\d{9,15}$')
    phone = models.CharField(validators=[phone_regex], max_length=17, verbose_name=_('your phone number'))
    date = models.DateTimeField(auto_now_add=True, verbose_name=_('date of Registration'))

    class Meta:
        ordering = ('-id',)
        verbose_name = _('Consultation request')
        verbose_name_plural = _('Consultation request')
    
    def __str__(self) -> str:
        return f'{self.name}-{self.phone}'


class ContactUs(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('your name'))
    email = models.EmailField(verbose_name=_('your email'))
    subject = models.CharField(max_length=300, verbose_name=_('subject'))
    message = models.TextField(verbose_name=_('message'))
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = _('contact us')
        verbose_name_plural = _('contact us')
        ordering = ('-id',)

    def __str__(self) -> str:
        return f'{self.name}-{self.email}'

