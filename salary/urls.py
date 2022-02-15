from django.urls import path


from .views import HomePageView, SalaryPostDetail, SalaryPage, IndustryListPage, JobBoardPage, CreateJobPost, Industry_JobBoardPage

app_name = 'salary'

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home_page'),
    path('salary-post/<int:pk>/', SalaryPostDetail.as_view(), name='salary_post_detail'),
    path('salary-page/', SalaryPage.as_view(), name='salary_page'),

    path('industry/', IndustryListPage.as_view(), name='industry_page'),

    path('job-board/', JobBoardPage.as_view(), name='job_board_page'),
    path('job-board-industry/<int:pk>/', Industry_JobBoardPage.as_view(), name='industry_job_board'),
    path('job-create/', CreateJobPost.as_view(), name='job-create'),
]
