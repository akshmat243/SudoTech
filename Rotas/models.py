from django.db import models
from django.utils import timezone


class Rota(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class WorkSchedule(models.Model):
    rota = models.ForeignKey(Rota, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=100)
    shift_start = models.DateTimeField()
    shift_end = models.DateTimeField()
    role = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee_name} ({self.rota.name})"


class Availability(models.Model):
    employee_name = models.CharField(max_length=100)
    date = models.DateField()
    is_available = models.BooleanField(default=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee_name} - {self.date} - {'Available' if self.is_available else 'Unavailable'}"
