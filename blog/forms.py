from django import forms 

from .models import IndustryBlog

class IndustryBlogForm(forms.ModelForm):
    class Meta:
        model = IndustryBlog
        exlcude = ['created_by','created_at', 'updated_at']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'industry': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Industry'}),
            'blog': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Blog'}),
        }   