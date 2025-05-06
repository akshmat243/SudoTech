from django.contrib import admin
from .models import Employee, Department, Designation

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'employee_id', 'first_name', 'last_name', 'email',
        'department', 'designation', 'date_joined', 'status'
    )
    search_fields = ('employee_id', 'first_name', 'last_name', 'email')
    list_filter = ('department', 'designation', 'status', 'gender', 'date_joined')
    readonly_fields = ('employee_id', 'created_at', 'updated_at')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')
    list_filter = ('department',)
