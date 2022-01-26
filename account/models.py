from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


from django.utils.translation import gettext_lazy as _ 

from .manager import CustomUserManager



class CustomUser(AbstractBaseUser, PermissionsMixin):

    # User Details

    email           = models.EmailField(_('Email Address'), unique=True)
    username        = models.CharField(max_length=15, unique=True, blank=True, null=True)
    
    first_name      = models.CharField(max_length=20)
    last_name       = models.CharField(max_length=20)

    birthday        = models.DateField(null=True, blank=True)

    # User Status
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    # Creation Info
    date_created    = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = CustomUserManager()
    

    class Meta:
        verbose_name            = 'Account'
        verbose_name_plural     = 'Accounts'

    def __str__(self):
        return self.email
        