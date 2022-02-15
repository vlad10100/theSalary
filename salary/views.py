from django.shortcuts import render
from django.http import HttpResponse

from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.views.generic import (CreateView, DetailView, ListView,
                                UpdateView, TemplateView, DeleteView,
                                FormView)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from account.models import UserProfile
from .models import Industry, JobBoard

from .forms import CreateJobForm


class HomePageView(LoginRequiredMixin, ListView):                                                            # retrieve all
    template_name = 'home.html'
    queryset = UserProfile.objects.all()

    def get_context_data(self, **kwargs):
        id_list = UserProfile.objects.values('id')
        query = {'id':self.request.user.id}
        print(query)
        # print(id_list)
        context = super().get_context_data(**kwargs)
        context['id_list'] = id_list
        context['query'] = query
        print(self.request.user.id)
        context['list'] = UserProfile.objects.all().exclude(id=self.request.user.id)
        return context


class SalaryPostDetail(LoginRequiredMixin, DetailView):
    template_name = 'salary_blog/salary_post_detail.html'
    context_object_name = 'post'
    queryset = UserProfile.objects.all()

    def get_object(self, **kwargs):
        post_id = self.kwargs['pk']
        return UserProfile.objects.get(id=post_id)



class SalaryPage(LoginRequiredMixin, ListView):
    template_name = 'salary_blog/salary_page.html'
    queryset = UserProfile.objects.all()
    # No context yet...


class IndustryListPage(LoginRequiredMixin, ListView):
    template_name = 'industry/industry_page.html'
    queryset = Industry.objects.all()
    context_object_name = 'industries'


class JobBoardPage(LoginRequiredMixin, ListView):
    template_name = 'job_board/job_board_page.html'
    queryset = JobBoard.objects.all()
    context_object_name = 'jobs'


class CreateJobPost(LoginRequiredMixin, CreateView):
    template_name = 'job_board/create_job.html' 
    form_class = CreateJobForm 
    success_url = reverse_lazy('salary:job_board_page')
