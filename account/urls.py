from django.urls import path 

from .views import (SignUpView, UserProfile_Create, 
                UserLoginView, UserProfile_Update, 
                UserProfile_Detail, CustomUser_Update, CustomUser_Delete,
                PasswordResetView, PasswordResetDoneView,
                PasswordResetConfirmView, PasswordResetCompleteView)


app_name = 'account'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup_view'),
    path('', UserLoginView.as_view(), name='user_login'),
    path('create-profile/', UserProfile_Create.as_view(), name='userprofile_create'),
    path('update-customprofile/', CustomUser_Update.as_view(), name='update_custom_user'),
    path('update-profile/', UserProfile_Update.as_view(), name='userprofile_update'),
    path('detail-profile/', UserProfile_Detail.as_view(), name='userprofile_detail'),   
    path('delete-account/', CustomUser_Delete.as_view(), name='delete_custom_user'),    


    # Password Reset
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]