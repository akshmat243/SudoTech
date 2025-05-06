from django.db import models
from django.utils import timezone

class MeasurementProfile(models.Model):
    customer_name = models.CharField(max_length=100)
    chest = models.DecimalField(max_digits=5, decimal_places=2)
    waist = models.DecimalField(max_digits=5, decimal_places=2)
    hips = models.DecimalField(max_digits=5, decimal_places=2)
    shoulder_width = models.DecimalField(max_digits=5, decimal_places=2)
    sleeve_length = models.DecimalField(max_digits=5, decimal_places=2)
    inseam = models.DecimalField(max_digits=5, decimal_places=2)
    additional_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Measurement Profile for {self.customer_name}"

class DesignType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class WorkType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class FabricType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Tailor(models.Model):
    name = models.CharField(max_length=100)
    skills = models.TextField()
    availability = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    order_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateField()
    measurement_profile = models.ForeignKey(MeasurementProfile, on_delete=models.CASCADE)
    design_type = models.ForeignKey(DesignType, on_delete=models.SET_NULL, null=True)
    work_type = models.ForeignKey(WorkType, on_delete=models.SET_NULL, null=True)
    fabric_type = models.ForeignKey(FabricType, on_delete=models.SET_NULL, null=True)
    tailor_assigned = models.ForeignKey(Tailor, on_delete=models.SET_NULL, null=True)
    collection_assigned = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True)
    status_choices = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]
    status = models.CharField(max_length=15, choices=status_choices, default='pending')
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Order for {self.customer_name} - {self.status}"
