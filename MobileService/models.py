from django.db import models
from django.utils import timezone


class SLAPolicy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    response_time_hours = models.PositiveIntegerField()
    resolution_time_hours = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ServiceContract(models.Model):
    customer_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    sla_policy = models.ForeignKey(SLAPolicy, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} Contract"


class PendingRequest(models.Model):
    customer_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    issue_description = models.TextField()
    date_requested = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pending - {self.customer_name}"


class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('Assigned', 'Assigned'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    ]

    customer_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    issue_description = models.TextField()
    service_contract = models.ForeignKey(ServiceContract, on_delete=models.SET_NULL, null=True, blank=True)
    sla_policy = models.ForeignKey(SLAPolicy, on_delete=models.SET_NULL, null=True, blank=True)
    date_requested = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Assigned')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} - {self.status}"


class ServiceHistory(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    service_notes = models.TextField()
    date_serviced = models.DateTimeField(default=timezone.now)
    technician_name = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"History for {self.service_request.customer_name}"


class SystemSetup(models.Model):
    company_name = models.CharField(max_length=255)
    support_email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
