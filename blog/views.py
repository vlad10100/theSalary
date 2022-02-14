from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from .forms import IndustryBlogForm, UpdateIndustryBlogForm

from .models import IndustryBlog
from account.models import CustomUser
from salary.models import Industry


class CreateIndustryBlog(CreateView):
    template_name = 'blog/create_blog.html'
    form_class = IndustryBlogForm
    queryset = IndustryBlog.objects.all()


    def form_valid(self, form):
        user = self.request.user
        form.instance.created_by = user
        print(user, '*')
        print(form.instance.industry)
        industry = form.instance.industry
        query = Industry.objects.get(industry=industry)
        query_id = query.id
        url = ('/blog/industry/%s'%(str(query_id)))
        form.save()
        return redirect(url)
    
    # def get_queryset(self):
    #     user = self.request.created_by
    #     print(UserProfile.objects.get(email=created_by), '**')
    #     return UserProfile.objects.get(email=created_by)

    # def get_object(self):
    #     print(self.request.created_by,'***')
    #     return self.request.created_by


class UpdateIndustryBlog(UpdateView):
    template_name = 'blog/update_blog.html'
    form_class = UpdateIndustryBlogForm
    queryset = IndustryBlog.objects.all()
    success_url = reverse_lazy('salary:home_page')

    def get_context_data(self, **kwargs):
        item = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        # context['user'] = self.request.user
        context['update'] = IndustryBlog.objects.get(id=item)
        return context



class DeleteIndustryBlog(DeleteView):
    template_name = 'blog/confirm_deletion.html'
    queryset = IndustryBlog.objects.all()
    success_url = reverse_lazy('salary:home_page')
    context_object_name = 'delete'

    def get_context_data(self, **kwargs):
        item = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        # context['user'] = self.request.user
        context['delete'] = IndustryBlog.objects.get(id=item)
        return context




class ListIndustryBlog(ListView):
    template_name = 'blog/x_industry_blog.html'
    model = IndustryBlog
    queryset = IndustryBlog.objects.all()

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['industry'] = Industry.objects.get(id=pk)
        cat = Industry.objects.get(id=pk)
        context['blogs'] = IndustryBlog.objects.filter(industry=cat)
        return context

