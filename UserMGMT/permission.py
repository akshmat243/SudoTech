from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied, ImproperlyConfigured
from .models import UserRole
from django.contrib.auth.models import Permission

class RolePermissionRequiredMixin:
    required_permissions = None
    required_roles = None

    def dispatch(self, request, *args, **kwargs):
        user = request.user

        if user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        if not user.is_authenticated:
            return redirect('login')

        user_roles_qs = UserRole.objects.select_related('role').filter(user=user, is_approved=True)
        role_names = {ur.role.name.lower() for ur in user_roles_qs}
        permissions = {perm.codename for ur in user_roles_qs for perm in ur.role.permission.all()}

        if self.required_permissions:
            required_perms = (
                [self.required_permissions]
                if isinstance(self.required_permissions, str)
                else self.required_permissions
            )

            all_valid_perms = set(Permission.objects.values_list('codename', flat=True))
            invalid_perms = [perm for perm in required_perms if perm not in all_valid_perms]
            if invalid_perms:
                raise ImproperlyConfigured(f"Invalid permission codename(s): {invalid_perms}")

            if not any(perm in permissions for perm in required_perms):
                raise PermissionDenied("Missing required permission.")

        if self.required_roles:
            required_roles = (
                [self.required_roles]
                if isinstance(self.required_roles, str)
                else self.required_roles
            )

            if not any(role.lower() in role_names for role in required_roles):
                raise PermissionDenied("Missing required role.")


        return super().dispatch(request, *args, **kwargs)
