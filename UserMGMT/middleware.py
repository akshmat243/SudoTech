from django.urls import resolve
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.contrib.auth.models import Permission
from .models import UserRole

EXEMPT_PATHS = [
    '/UserMGMT/login/',
    '/UserMGMT/register/',
    '/UserMGMT/logout/',
    '/admin/login/',
    '/admin/',
    '/allauth.socialaccount.providers.google/google/login/',
]

class RolePermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path_info.startswith(tuple(EXEMPT_PATHS)):
            return self.get_response(request)

        if not request.user.is_authenticated:
            return redirect('/UserMGMT/login/')

        if request.user.is_superuser:
            return self.get_response(request)

        try:
            resolver_match = resolve(request.path_info)
        except Exception:
            return HttpResponseForbidden("Forbidden: URL could not be resolved.")

        app_label = resolver_match.app_name or resolver_match.func.__module__.split('.')[0]
        url_name = resolver_match.url_name or ''
        model_name = url_name.split('_')[-1] if '_' in url_name else None

        method = request.method.lower()
        action_map = {
            'get': 'view',
            'post': 'add',
            'put': 'change',
            'patch': 'change',
            'delete': 'delete',
        }
        action = action_map.get(method, 'view')

        if not model_name:
            return self.get_response(request)

        codename = f"{action}_{model_name}"

        # Get user's approved roles
        approved_roles = UserRole.objects.filter(user=request.user, is_approved=True).select_related('role')
        if not approved_roles.exists():
            return HttpResponseForbidden("You do not have any approved role.")

        # Get all permissions from all approved roles
        role_ids = [ur.role.id for ur in approved_roles]
        allowed_perms = Permission.objects.filter(role__id__in=role_ids)

        if not allowed_perms.filter(codename=codename, content_type__app_label=app_label).exists():
            return HttpResponseForbidden("You do not have permission to access this page.")

        return self.get_response(request)
