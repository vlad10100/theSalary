from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.views.generic import (CreateView, DetailView, ListView,
                                UpdateView, TemplateView, DeleteView,
                                FormView)

from account.forms import LoginForm
from .forms import SalaryBlog_Form
from .models import SalaryBlog



class LoginLandingPageView(LoginView):
    template_name = 'landing_page.html'
    fields = ['email', 'password']
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('salary:home_page')




class HomePageView(ListView):                       # retrieve all
    template_name = 'home.html'
    context_object_name = 'list'
    queryset = SalaryBlog.objects.all()

    


    
class CreateSalaryBlog(CreateView):                 # create
    template_name = 'salary_blog/create_post.html'
    form_class = SalaryBlog_Form
    queryset = SalaryBlog.objects.all()
    success_url = reverse_lazy('salary:home_page')


class UpdateSalaryBlog(UpdateView):                 # update
    template_name = 'salary_blog/update_post.html'
    form_class = SalaryBlog_Form
    queryset = SalaryBlog.objects.all()
    success_url = reverse_lazy('salary:home_page')


class DeleteSalaryBlog(DeleteView):                 # confirm deletion
    template_name = 'salary_blog/delete_post.html'
    queryset = SalaryBlog.objects.all()
    success_url = reverse_lazy('salary:home_page')


class SalaryBlogDetail(DetailView):                 # specific blog detail
    template_name = 'salary_blog/post_detail.html'
    queryset = SalaryBlog.objects.all()
    context_object_name = 'list'