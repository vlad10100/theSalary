from django.shortcuts import render
from django.http import HttpResponse

from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.views.generic import (CreateView, DetailView, ListView,
                                UpdateView, TemplateView, DeleteView,
                                FormView)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from account.models import UserProfile
from .models import Industry



class HomePageView(ListView):                                                            # retrieve all
    template_name = 'home.html'
    context_object_name = 'list'
    queryset = UserProfile.objects.all()

    def get_context_data(self, **kwargs):
        id_list = UserProfile.objects.values('id')
        # id_list -->>>  <QuerySet [{'id': 4}, {'id': 7}, {'id': 3}, {'id': 6}, {'id': 1}, {'id': 2}, {'id': 5}]>
        print(id_list)
        query = {'id':self.request.user.id}
        context = super().get_context_data(**kwargs)
        context['id_list'] = id_list
        context['query'] = query
        return context


class SalaryPostDetail(DetailView):
    template_name = 'salary_blog/salary_post_detail.html'
    context_object_name = 'post'
    queryset = UserProfile.objects.all()



class SalaryPage(ListView):
    template_name = 'salary_blog/salary_page.html'
    queryset = UserProfile.objects.all()
    # No context yet...


class IndustryListPage(ListView):
    template_name = 'industry/industry_page.html'
    queryset = Industry.objects.all()
    context_object_name = 'industries'