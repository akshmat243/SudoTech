from django.db import models
from UserMGMT.models import User


class BiometricDevice(models.Model):
    device_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.device_name} - {self.location}"


class BiometricAttendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
        ('on_leave', 'On Leave'),
    ]

    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.TimeField(blank=True, null=True)
    check_out = models.TimeField(blank=True, null=True)
    total_hours = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='present')
    device = models.ForeignKey(BiometricDevice, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('employee', 'date')

    def __str__(self):
        return f"{self.employee} - {self.date} - {self.status}"
