from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('verify-email/<uidb64>/<token>/', verify_email, name='verify-email'),
    path('registration-email-sent/', TemplateView.as_view(template_name='emails/email_sent.html'), name='registration_email_sent'),


]