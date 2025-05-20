"""
URL configuration for Dash project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import importlib
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from UserMGMT.views import (
    DynamicCreateView, DynamicDeleteView, DynamicListView, DynamicUpdateView
)
    
    
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("accounts/", include('allauth.urls')),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('perms/<str:app_label>/<str:model_name>/', DynamicListView.as_view(), name='dynamic_list'),
    path('perms/<str:app_label>/<str:model_name>/add/', DynamicCreateView.as_view(), name='dynamic_add'),
    path('perms/<str:app_label>/<str:model_name>/<int:pk>/edit/', DynamicUpdateView.as_view(), name='dynamic_edit'),
    path('perms/<str:app_label>/<str:model_name>/<int:pk>/delete/', DynamicDeleteView.as_view(), name='dynamic_delete'),

]

for app in settings.INSTALLED_APPS:
    try:
        importlib.import_module(f'{app}.urls')
        urlpatterns.append(path(f'{app}/', include(f'{app}.urls')))
    except ModuleNotFoundError:
        pass
