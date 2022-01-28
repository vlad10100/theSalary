from django.conf import settings

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.views.generic import CreateView
from .forms import CustomUserCreationForm





class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = CustomUserCreationForm 

    def get_success_url(self):
        return reverse_lazy('salary:home_page')


