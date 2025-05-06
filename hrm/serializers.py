from rest_framework import serializers
from .models import Department, Designation, Employee


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class DesignationSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = Designation
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    designation = DesignationSerializer(read_only=True)
    photo = serializers.ImageField(required=False)
    resume = serializers.FileField(required=False)

    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ['employee_id']
