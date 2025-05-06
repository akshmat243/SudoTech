from rest_framework import serializers
from .models import Service, Package, Customer, Appointment, Billing


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class PackageSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)
    service_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Service.objects.all(), write_only=True, source='services'
    )

    class Meta:
        model = Package
        fields = ['id', 'name', 'description', 'total_price', 'services', 'service_ids']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.name', read_only=True)
    service_name = serializers.CharField(source='service.name', read_only=True)
    package_name = serializers.CharField(source='package.name', read_only=True)

    class Meta:
        model = Appointment
        fields = '__all__'


class BillingSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='appointment.customer.name', read_only=True)
    scheduled_datetime = serializers.DateTimeField(source='appointment.scheduled_datetime', read_only=True)

    class Meta:
        model = Billing
        fields = '__all__'
