from .models import UserRole, ModelAccess, RoleModelPermission

def has_permission(user, app_label, model_name, action):
    try:
        role = UserRole.objects.get(user=user).role
        model = ModelAccess.objects.get(module__name=app_label, model_name=model_name)
        perm = RoleModelPermission.objects.get(role=role, model_access=model)
        return getattr(perm, f"can_{action}")
    except Exception:
        return False
