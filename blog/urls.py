from django.urls import path 

from .views import CreateIndustryBlog, UpdateIndustryBlog, DeleteIndustryBlog

app_name = 'blog'

urlpatterns = [
    path('create_blog/', CreateIndustryBlog.as_view(), name='create_blog'),
    path('update_blog/<int:pk>/', UpdateIndustryBlog.as_view(), name='update_blog'),
    path('delete_blog/<int:pk>/', DeleteIndustryBlog.as_view(), name='delete_blog'),
]
