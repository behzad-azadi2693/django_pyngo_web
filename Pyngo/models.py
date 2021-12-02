from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام')
    phone_regex = RegexValidator(regex=r'^\d{9,15}$')
    phone = models.CharField(validators=[phone_regex], max_length=17, verbose_name="تلفن")
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')

    class Meta:
        ordering = ('-id',)

    def __str__(self) -> str:
        return f'{self.name}-{self.phone}'


class ContactUs(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    subject = models.CharField(max_length=300, verbose_name='موضوع')
    message = models.TextField(verbose_name='پیغام')
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'پیغام'
        verbose_name_plural = 'پیغام ها'
        ordering = ('-id',)

    def __str__(self) -> str:
        return f'{self.name}-{self.email}'

