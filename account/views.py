from django.conf import settings

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.views import LoginView

from .models import UserProfile

from .forms import CustomUserCreationForm, UserProfile_Form, CustomUser_UpdateForm





class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = CustomUserCreationForm 

    def get_success_url(self):
        return reverse_lazy('salary:home_page')


class UserLoginView(LoginView):
    template_name = 'landing_page.html'
    fields = ['email', 'password']
    redirect_authenticated_user = True  

    def success_url(self):
        return reverse_lazy('salary:home_page')


class UserProfile_Create(CreateView): # unique constraint ! ! !
    template_name = 'profile/create_profile.html'
    form_class = UserProfile_Form
    success_url = reverse_lazy('salary:home_page')
    context_object_name = 'loggedin_user'
    
    def form_valid(self, form):
        user = self.request.user 
        form.instance.user = user 
        return super(UserProfile_Create, self).form_valid(form)
    
    def get_queryset(self):
        user = self.request.user
        return UserProfile.objects.get(email=user)

    def get_object(self):
        return self.request.user.userprofile


class CustomUser_Update(UpdateView):
    template_name = 'profile/update_custom_user.html'
    form_class = CustomUser_UpdateForm
    success_url = reverse_lazy('salary:home_page')

    def get_object(self):
        return self.request.user

    
    

class UserProfile_Update(UpdateView):
    template_name = 'profile/update_profile.html'
    form_class = UserProfile_Form
    success_url = reverse_lazy('salary:home_page')

    def get_object(self):
        return self.request.user.userprofile
    

# User's personal details
class UserProfile_Detail(DetailView):
    template_name = 'profile/detail_profile.html'
    queryset = UserProfile.objects.all()

    def get_object(self):
        return self.request.user.userprofile