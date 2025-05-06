from django.db import models
from django.utils import timezone

class CollectionRequest(models.Model):
    customer_name = models.CharField(max_length=255)
    address = models.TextField()
    collection_date = models.DateField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending')
    request_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Collection Request by {self.customer_name} on {self.collection_date}"

class Trip(models.Model):
    collection_request = models.ForeignKey(CollectionRequest, on_delete=models.CASCADE)
    driver_name = models.CharField(max_length=255)
    vehicle_number = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('in-progress', 'In Progress'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='in-progress')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Trip for {self.collection_request.customer_name} - {self.status}"

class Inspection(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    inspector_name = models.CharField(max_length=255)
    inspection_date = models.DateTimeField(default=timezone.now)
    findings = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('approved', 'Approved'), ('rejected', 'Rejected'), ('pending', 'Pending')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Inspection for Trip {self.trip.id} - {self.status}"


class CollectionSchedule(models.Model):
    day_of_week = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    assigned_driver = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Collection Schedule - {self.day_of_week} from {self.start_time} to {self.end_time}"


class DisposalFacility(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.DecimalField(max_digits=10, decimal_places=2)  # in tons
    contact_info = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Recycling(models.Model):
    material_type = models.CharField(max_length=100)
    quantity_collected = models.DecimalField(max_digits=10, decimal_places=2)  # in kg
    collection_date = models.DateField()
    recycling_center = models.ForeignKey(DisposalFacility, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.material_type} - {self.quantity_collected} kg"


class SystemSetup(models.Model):
    system_name = models.CharField(max_length=255)
    configuration_details = models.TextField()
    setup_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"System Setup for {self.system_name} on {self.setup_date}"
