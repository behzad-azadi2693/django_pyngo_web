from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime, timedelta

class MyUserManager(BaseUserManager):
    def create_user(self, username, password):
        if not username:
            raise ValueError('لطفا شماره خود را وارد کنید')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return UserWarning

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=17, unique=True, verbose_name='نام کاربری')
    email = models.EmailField(verbose_name='ایمیل شما') 


    is_active = models.BooleanField(default=True, verbose_name='کاربر فعال باشد؟')
    is_admin = models.BooleanField(default=False, verbose_name='کاربر ادمین باشد؟')
    

    objects = MyUserManager()
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self) -> str:
        return f'نام کاربری:{self.username}'

    def has_perm(self, perm, obj=None) -> bool:
        return True

    def has_module_perms(self, app_label) -> bool:
        return True

    @property
    def is_staff(self):
        return self.is_admin

