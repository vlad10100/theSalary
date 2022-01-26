from django.contrib import admin

from .models import CustomUser, SalaryBlog, Industry, Job

admin.site.register(CustomUser)
admin.site.register(Industry)
admin.site.register(Job)
admin.site.register(SalaryBlog)