from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='user-register'),
    path('assign-role/<int:pk>/', AssignRoleView.as_view(), name='assign-role'),
    path('roles/', RoleListCreateView.as_view(), name='role-list-create'),

]