from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Role, Module, ModelAccess, Role, RoleModelPermission, UserRole

class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    list_display = ['email', 'name', 'workspace_name', 'is_staff', 'is_superuser']
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    search_fields = ['email', 'name', 'workspace_name']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'workspace_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'workspace_name', 'password1', 'password2'),
        }),
    )

admin.site.register(User, UserAdmin)



@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page = 25


@admin.register(ModelAccess)
class ModelAccessAdmin(admin.ModelAdmin):
    list_display = ('id', 'module', 'model_name')
    list_filter = ('module',)
    search_fields = ('module__name', 'model_name')
    ordering = ('module__name', 'model_name')
    list_per_page = 25


class RoleModelPermissionInline(admin.TabularInline):
    model = RoleModelPermission
    extra = 1
    autocomplete_fields = ['model_access']
    fields = ('model_access', 'can_manage', 'can_create', 'can_edit', 'can_delete')
    show_change_link = True


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    inlines = [RoleModelPermissionInline]
    list_per_page = 25


@admin.register(RoleModelPermission)
class RoleModelPermissionAdmin(admin.ModelAdmin):
    list_display = (
        'role', 'model_access', 'can_manage', 'can_create', 'can_edit', 'can_delete'
    )
    list_filter = ('role', 'model_access__module')
    search_fields = ('role__name', 'model_access__model_name', 'model_access__module__name')
    autocomplete_fields = ['role', 'model_access']
    list_per_page = 25


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)
    search_fields = ('user__username', 'user__email', 'role__name')
    autocomplete_fields = ['user', 'role']
    list_per_page = 25
