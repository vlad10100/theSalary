from django.contrib import admin

from .models import SalaryBlog, Industry, Job

admin.site.register(Industry)
admin.site.register(Job)
admin.site.register(SalaryBlog)