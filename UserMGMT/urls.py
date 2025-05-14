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
     path('approve_role/<int:user_id>/<int:role_id>/', ApproveRoleView.as_view(), name='approve_role'),
    path('deactivate_user/<int:user_id>/', DeactivateUserView.as_view(), name='deactivate_user'),
    path('activate_user/<int:user_id>/', ActivateUserView.as_view(), name='activate_user'),
    path('update_module_access/<int:role_id>/<str:action>/', UpdateModuleAccessView.as_view(), name='update_module_access'),
    
    path('verify-email/<uidb64>/<token>/', verify_email, name='verify-email'),
    path('registration-email-sent/', TemplateView.as_view(template_name='emails/email_sent.html'), name='registration_email_sent'),

    path('forgot-password/', auth_views.PasswordResetView.as_view(template_name='auth-basic-forgot-password.html'), name='password_reset'),
    path('forgot-password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='auth-basic-reset-password.html'), name='password_reset_confirm'),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]