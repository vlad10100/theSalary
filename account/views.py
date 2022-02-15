from django.conf import settings

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.views import (LoginView, PasswordResetView, PasswordResetDoneView, 
                                        PasswordResetConfirmView, PasswordResetCompleteView)

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserProfile, CustomUser

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


class UserProfile_Create(LoginRequiredMixin, CreateView):
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


class CustomUser_Update(LoginRequiredMixin, UpdateView):
    template_name = 'profile/update_custom_user.html'
    form_class = CustomUser_UpdateForm
    success_url = reverse_lazy('salary:home_page')

    def get_object(self):
        return self.request.user

    
class UserProfile_Update(LoginRequiredMixin, UpdateView):
    template_name = 'profile/update_profile.html'
    form_class = UserProfile_Form
    success_url = reverse_lazy('salary:home_page')

    def get_object(self):
        return self.request.user.userprofile
    

class CustomUser_Delete(LoginRequiredMixin, DeleteView):
    template_name = 'profile/delete_custom_user.html'
    success_url = reverse_lazy('salary:home_page')
    
    def get_object(self):
        return self.request.user




# User's personal details
class UserProfile_Detail(LoginRequiredMixin, DetailView):
    template_name = 'profile/detail_profile.html'
    queryset = UserProfile.objects.all()

    def get_object(self):
        id_num = self.request.user.id
        find = {'id':id}
        if find not in UserProfile.objects.values('id'):
            print('not here')
            return reverse_lazy('account:userprofile_create')
        else:
            print('here')
            return self.request.user.userprofile



class PasswordResetView(PasswordResetView):
    template_name = 'password_reset/reset_view.html'
    email_template_name = 'password_reset/password_reset_email.html'
    success_url = reverse_lazy('account:password_reset_done')

class PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset/reset_done_view.html'

class PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset/reset_confirm_view.html'
    success_url = reverse_lazy('account:password_reset_complete')

class PasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset/reset_complete_view.html'