from django.db import models
from django.utils import timezone


class GardenBed(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    size_sq_meters = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Plant(models.Model):
    name = models.CharField(max_length=100)
    bed = models.ForeignKey(GardenBed, on_delete=models.CASCADE)
    planted_on = models.DateField()
    plant_type = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class WateringSchedule(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    frequency_days = models.PositiveIntegerField()
    last_watered = models.DateField()
    next_due = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Water {self.plant.name} every {self.frequency_days} days"


class MaintenanceLog(models.Model):
    bed = models.ForeignKey(GardenBed, on_delete=models.CASCADE)
    performed_on = models.DateField(default=timezone.now)
    activity = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.activity} on {self.bed.name}"


class SeasonalPlan(models.Model):
    season = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    planned_activities = models.TextField()
    planned_crops = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.season} {self.year}"


class PestAndDisease(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    issue_type = models.CharField(max_length=100, choices=[("pest", "Pest"), ("disease", "Disease")])
    description = models.TextField()
    date_detected = models.DateField()
    action_taken = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.issue_type.capitalize()} on {self.plant.name}"
