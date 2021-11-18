from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime, timedelta

class MyUserManager(BaseUserManager):
    def create_user(self, phone, password):
        if not phone:
            raise ValueError('لطفا شماره خود را وارد کنید')
        user = self.model(phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phone, password):
        user = self.create_user(phone=phone, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return UserWarning

class User(AbstractBaseUser, PermissionsMixin):

    phone_regex = RegexValidator(regex=r'^\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, unique=True, verbose_name="your phone number") 
    otp = models.PositiveIntegerField(null=True, blank=True)
    otp_create_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    is_active = models.BooleanField(default=True, verbose_name='کاربر فعال باشد؟')
    is_admin = models.BooleanField(default=False, verbose_name='کاربر ادمین باشد؟')
    phone_check = models.BooleanField(default=False, verbose_name = 'تلفن تایید شده؟')

    objects = MyUserManager()
    USERNAME_FIELD = 'phone'

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self) -> str:
        return f'نام کاربری:{self.phone}'

    def has_perm(self, perm, obj=None) -> bool:
        return True

    def has_module_perms(self, app_label) -> bool:
        return True

    @property
    def is_staff(self):
        return self.is_admin

