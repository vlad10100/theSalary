from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (CreateView, DetailView, ListView,
                                UpdateView, TemplateView, DeleteView)


class LandingPageView(TemplateView):
    template_name = 'landing_page.html'

class HomePageView(ListView):
    template_name = 'home.html'

class CreateSalaryBlog(CreateView):
    template_name = 'salary_blog/create_post.html'

class UpdateSalaryBlog(UpdateView):
    template_name = 'salary_blog/update_post.html'

class DeleteSalaryBlog(DeleteView):
    template_name = 'salary_blog/delete_post.html'

class SalaryBlogDetail(CreateView):
    template_name = 'salary_blog/post_detail.html'