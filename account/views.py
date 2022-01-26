from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView 
from django.contrib.auth.views import LoginView

from .forms import CustomUserCreationForm








class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = CustomUserCreationForm 

    def get_success_url(self):
        return reverse_lazy('account:signup_view')

