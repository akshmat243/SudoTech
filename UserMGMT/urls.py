from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),



    path('api/assign-role/<int:pk>/', AssignRoleView.as_view(), name='assign-role'),
    path('api/roles/', RoleListCreateView.as_view(), name='role-list-create'),

]