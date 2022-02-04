from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


from django.utils.translation import gettext_lazy as _ 

from .manager import CustomUserManager

from salary.models import Industry

from datetime import datetime



class CustomUser(AbstractBaseUser, PermissionsMixin):

    # User Details

    email           = models.EmailField(_('Email Address'), unique=True)
    username        = models.CharField(max_length=15, unique=True, blank=True, null=True)

    profile_picture = models.ImageField(upload_to='images/', default='user.png')

    first_name      = models.CharField(max_length=20)
    last_name       = models.CharField(max_length=20)

    birthday        = models.DateField(null=True, blank=True)

    is_anonymous    = models.BooleanField(default=True)
    is_recruiter    = models.BooleanField(default=False)
    is_common_user  = models.BooleanField(default=True)


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
        

        
class UserProfile(models.Model):
    DEGREE_PROGRAM = [
        ('ME','Mechanical Engineering'),
        ('CE','Civil Engineering'),
        ('EE','Electrical Engineering'),
        ('ECE','Electronics and Communication Engineering'),
        ('ChE','Chemical Engineering'),
    ]

    GENDER = [
        ('M','Male'),
        ('F','Female'),
        ('U','Undefined')
    ]

    CIVIL_STATUS = [
        ('Single','Single'),
        ('Married','Married'),
        ('Divorced','Divorced'),
    ]


    position                    = models.CharField(max_length=50, null=False, blank=False)
    degree_program              = models.CharField(max_length=5, choices=DEGREE_PROGRAM, null=False, blank=False)
    gender                      = models.CharField(max_length=1, choices=GENDER)
    civil_status                = models.CharField(max_length=10, choices=CIVIL_STATUS)
    yoe                         = models.PositiveSmallIntegerField(null=False, blank=False)
    tool_1                      = models.CharField(max_length=20, null=False, blank=False)
    tool_2                      = models.CharField(max_length=20, null=True, blank=True)
    tool_3                      = models.CharField(max_length=20, null=True, blank=True)
    salary                      = models.PositiveIntegerField(null=False, blank=False)
    location                    = models.CharField(max_length=50, null=False, blank=False)

    industry                    = models.ForeignKey(Industry, on_delete=models.CASCADE)

    user                        = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
 
    created                     = models.DateTimeField(auto_now_add=True)
    updated                     = models.DateTimeField(auto_now=True)


    class Meta:
        
        verbose_name            = 'Salary Info'
        verbose_name_plural     = 'Salary Info'



    def __repr__(self):
        output = f"{self.user.username} || {self.position} || {self.salary} || {self.location}"
        return output
    
    def __str__(self):
        return self.__repr__()


