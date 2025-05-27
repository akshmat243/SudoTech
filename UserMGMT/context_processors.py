from .models import UserRole  # Adjust import
from django.apps import apps
from django.contrib.auth.models import Permission

def global_data(request):
    user = request.user
    if user.is_authenticated:
        user_roles_qs = UserRole.objects.select_related('role').filter(user=user, is_approved=True)
        role_permissions = set(
            perm for ur in user_roles_qs for perm in ur.role.permission.all()
        )
        role_permission_codenames = set(perm.codename for perm in role_permissions)

        # Build app_list (sidebar permissions) here
        app_list = []
        for app_config in apps.get_app_configs():
            models = []
            for model in app_config.get_models():
                model_name = model._meta.model_name

                crud_permission_codenames = {
                    f"add_{model_name}",
                    f"view_{model_name}",
                    f"change_{model_name}",
                    f"delete_{model_name}",
                }

                model_permissions = Permission.objects.filter(
                    content_type__app_label=app_config.label,
                    content_type__model=model_name,
                    codename__in=crud_permission_codenames
                )

                if not user.is_superuser:
                    model_permissions = [perm for perm in model_permissions if perm in role_permissions]

                if model_permissions:
                    perms_list = []
                    for perm in model_permissions:
                        try:
                            model_name_from_perm = perm.codename.split('_', 1)[1]
                        except IndexError:
                            model_name_from_perm = model_name

                        perms_list.append({
                            'name': perm.name,
                            'codename': perm.codename,
                            'model_name_from_perm': model_name_from_perm,
                        })

                    models.append({
                        'model_name': model_name,
                        'permissions': perms_list,
                    })

            if models:
                app_list.append({
                    'app_label': app_config.label,
                    'models': models
                })

        return {
            'current_username': user.username,
            'current_user_roles': [ur.role.name for ur in user_roles_qs],
            'assigned_permissions': role_permission_codenames,
            'app_list': app_list,
        }

    else:
        return {
            'current_username': None,
            'current_user_roles': [],
            'assigned_permissions': set(),
            'app_list': [],
        }

