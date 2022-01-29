from django.shortcuts import render
from django.http import HttpResponse

from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.views.generic import (CreateView, DetailView, ListView,
                                UpdateView, TemplateView, DeleteView,
                                FormView)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from account.models import UserProfile



class HomePageView(ListView):                                           # retrieve all
    template_name = 'home.html'
    context_object_name = 'list'
    queryset = UserProfile.objects.all()


    





# class CreateSalaryBlog(LoginRequiredMixin, UserPassesTestMixin, CreateView):                 # create
#     template_name = 'salary_blog/create_post.html'
#     form_class = SalaryBlog_Form
#     raise_exception = True
#     queryset = SalaryBlog.objects.all()
#     success_url = reverse_lazy('salary:home_page')

#     def test_func(self):
#         if self.request.user.id in SalaryBlog.objects.values('user_id'):
#             print(self.request.user)
#             return True
#         else:
#             return False
        

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(CreateSalaryBlog, self).form_valid(form)


# class UpdateSalaryBlog(LoginRequiredMixin, UpdateView):                 # update
#     template_name = 'salary_blog/update_post.html'
#     form_class = SalaryBlog_Form
#     queryset = SalaryBlog.objects.all()
#     success_url = reverse_lazy('salary:home_page')



# class DeleteSalaryBlog(LoginRequiredMixin, DeleteView):                 # confirm deletion
#     template_name = 'salary_blog/delete_post.html'
#     queryset = SalaryBlog.objects.all()
#     success_url = reverse_lazy('salary:home_page')



# class SalaryBlogDetail(DetailView):                                     # specific blog detail
#     template_name = 'salary_blog/post_detail.html'
#     queryset = SalaryBlog.objects.all()
#     context_object_name = 'list'



# #                                   INDUSTRY 