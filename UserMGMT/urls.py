from django.urls import path
from .views import *
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('dashboard/', DashboardView.as_view(), name='dashboard'),
    
    path('dashboard/<str:username>', AdminDashboardView.as_view(), name='dashboard'),
    path('user-roles/', UserRoleListView.as_view(), name='user_role_list'),

    path('roles/create/', CreateRoleView.as_view(), name='create_role'),
    path('roles/', RoleListView.as_view(), name='role_list'),


    
    path('verify-email/<uidb64>/<token>/', verify_email, name='verify-email'),
    path('registration-email-sent/', TemplateView.as_view(template_name='emails/email_sent.html'), name='registration_email_sent'),

    path('forgot-password/', auth_views.PasswordResetView.as_view(template_name='auth/auth-basic-forgot-password.html'), name='password_reset'),
    path('forgot-password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='auth/auth-basic-reset-password.html'), name='password_reset_confirm'),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]