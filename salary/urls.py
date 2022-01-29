from django.urls import path


from .views import HomePageView, SalaryPostDetail, SalaryPage

app_name = 'salary'

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home_page'),
    path('salary-post/<int:pk>/', SalaryPostDetail.as_view(), name='salary_post_detail'),
    path('salary-page/', SalaryPage.as_view(), name='salary_page')    
]
