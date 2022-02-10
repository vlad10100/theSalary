from django import forms 

from .models import IndustryBlog

class IndustryBlogForm(forms.ModelForm):
    class Meta:
        model = IndustryBlog
        # fields= '__all__'
        exclude = ['created_by','created_at', 'updated_at']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'industry': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Industry'}),
            'blog': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Blog'}),
        }   

class UpdateIndustryBlogForm(forms.ModelForm):
    class Meta:
        model = IndustryBlog
        # fields= '__all__'
        exclude = ['created_by','created_at', 'updated_at', 'industry']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'blog': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Blog'}),
        }   