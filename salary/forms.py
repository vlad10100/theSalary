from django import forms

from .models import Industry, Job, SalaryBlog


class SalaryBlog_Form(forms.ModelForm):
    class Meta:
        model = SalaryBlog
        exclude = ('created', 'updated',)


