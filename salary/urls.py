from django.urls import path

from .views import (LandingPageView, HomePageView, CreateSalaryBlog,
                UpdateSalaryBlog, DeleteSalaryBlog, SalaryBlogDetail)

app_name = 'salary'

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('home/', HomePageView.as_view(), name='home_page'),
    path('create/', CreateSalaryBlog.as_view(), name='create_salary_blog'),
    path('update/', UpdateSalaryBlog.as_view(), name='update_salary_blog'),
    path('delete', DeleteSalaryBlog.as_view(), name='delete_salary_blog'),
    path('detail/', SalaryBlogDetail.as_view(), name='salary_blog_detail'),

    

]
