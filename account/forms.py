from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import CustomUser, UserProfile



class CustomUserCreationForm(forms.Form, UserCreationForm):

    class Meta:
        model = CustomUser 
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'is_recruiter',
            'is_common_user',
            'password1',
            'password2'
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email@email.com'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-enter password'})
        }

class CustomUser_UpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'birthday',
            'profile_picture',
            'is_anonymous',
            'is_recruiter',
            'is_common_user',
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'birthday': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Birthday', 'type':'date'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Profile Picture'}),
        }



class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser 
        fields = ['email', 'password']

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email@email.com'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        }


class UserProfile_Form(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['created', 'updated', 'user']

        widgets = {
            'industry': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Industry'}),
            'degree_program': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Degree Program'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Position'}),
            'civil_status': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Civil Status'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Gender'}),

            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'yoe': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Years of Experience'}),

            'tool_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'tool_1'}),
            'tool_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'tool_2'}),
            'tool_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'tool_3'}),

            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'salary'}),
        }


