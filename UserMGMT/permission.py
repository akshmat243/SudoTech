from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied, ImproperlyConfigured
from .models import UserRole
from django.contrib.auth.models import Permission

class RolePermissionRequiredMixin:
    required_permissions = None  # String or list
    required_roles = None        # String or list

    def dispatch(self, request, *args, **kwargs):
        # Superuser bypass
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        if not request.user.is_authenticated:
            return redirect('login')

        try:
            user_roles_qs = UserRole.objects.select_related('role').filter(user=request.user, is_approved=True)
            role_names = [ur.role.name.lower() for ur in user_roles_qs]
            permissions = set(perm.codename for ur in user_roles_qs for perm in ur.role.permission.all())

            # ✅ Validate required_permissions
            if self.required_permissions:
                required_perms = (
                    [self.required_permissions] if isinstance(self.required_permissions, str)
                    else self.required_permissions
                )

                all_valid_perms = set(Permission.objects.values_list('codename', flat=True))
                invalid_perms = [perm for perm in required_perms if perm not in all_valid_perms]

                if invalid_perms:
                    raise ImproperlyConfigured(f"Invalid permission codename(s): {invalid_perms}")

                if any(perm in permissions for perm in required_perms):
                    return super().dispatch(request, *args, **kwargs)

            # ✅ Role check
            if self.required_roles:
                required_roles = (
                    [self.required_roles] if isinstance(self.required_roles, str)
                    else self.required_roles
                )
                if any(role.lower() in role_names for role in required_roles):
                    return super().dispatch(request, *args, **kwargs)

        except Exception as e:
            # Optional: log exception here if needed
            pass

        raise PermissionDenied("You do not have permission to access this page.")
