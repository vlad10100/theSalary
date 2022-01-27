from django import forms

from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser



class CustomUserCreationForm(forms.Form, UserCreationForm):

    class Meta:
        model = CustomUser 
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'birthday',
            'password1',
            'password2'
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email@email.com'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'birthday': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
        }

