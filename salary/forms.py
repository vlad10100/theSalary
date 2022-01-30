from django import forms 

from .models import JobBoard


class CreateJobForm(forms.ModelForm):
    class Meta:
        model = JobBoard 
        fields = '__all__'
        # job_name, description, pay, industry

        widgets = {
            "industry": forms.Select(attrs={'class': 'form-control', 'placeholder': 'Industry'}),
            "job_name" : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Name'}),
            "description" : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            "pay" : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
        }
