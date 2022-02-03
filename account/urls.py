from django.urls import path 

from .views import SignUpView, UserProfile_Create, UserLoginView, UserProfile_Update, UserProfile_Detail, CustomUser_Update


app_name = 'account'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup_view'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('create-profile/', UserProfile_Create.as_view(), name='userprofile_create'),
    path('update-customprofile/', CustomUser_Update.as_view(), name='update_custom_user'),
    path('update-profile/', UserProfile_Update.as_view(), name='userprofile_update'),
    path('detail-profile/', UserProfile_Detail.as_view(), name='userprofile_detail'),       

]