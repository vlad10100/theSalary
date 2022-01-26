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

    birthday        = models.DateField()

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


class Industry(models.Model):
    industry                    = models.CharField(max_length=30, unique=True)
    
    class Meta:
        verbose_name            = 'Industy'
        verbose_name_plural     = 'Industries'

    def __repr__(self):
        return self.industry
    
    def __str__(self):
        return self.__repr__()

class Job(models.Model):
    job                         = models.CharField(max_length=30, unique=True)

    industry                    = models.ForeignKey('Industry', on_delete=models.CASCADE)

    class Meta:
        verbose_name            = 'Job'
        verbose_name_plural     = 'Jobs'

    

    def __repr__(self):
        return self.job
    
    def __str__(self):
        return self.__repr__()

class SalaryBlog(models.Model):
    position                    = models.CharField(max_length=50, null=False, blank=False)
    role                        = models.CharField(max_length=50, null=False, blank=False)
    yoe                         = models.PositiveSmallIntegerField(null=False, blank=False)
    tool_1                      = models.CharField(max_length=20, null=False, blank=False)
    tool_2                      = models.CharField(max_length=20, null=True, blank=True)
    tool_3                      = models.CharField(max_length=20, null=True, blank=True)
    salary                      = models.PositiveIntegerField(null=False, blank=False)
    location                    = models.CharField(max_length=50, null=False, blank=False)

    user                        = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    job                         = models.ForeignKey('Job', on_delete=models.CASCADE)


    class Meta:
        verbose_name            = 'Salary Info'
        verbose_name_plural     = 'Salary Info'



    def __repr__(self):
        output = f"{self.user.username} || {self.position} || {self.role} || {self.salary} || {self.location}"
        return output
    
    def __str__(self):
        return self.__repr__()
