from django.db import models
from django.utils import timezone


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    enrolled_date = models.DateField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    registration_number = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    type = models.CharField(max_length=50)  # e.g. Manual / Automatic
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.registration_number


class DrivingClass(models.Model):
    title = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    schedule = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    driving_class = models.ForeignKey(DrivingClass, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    duration_minutes = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.name} - {self.date}"


class Invoice(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    issue_date = models.DateField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Invoice #{self.id} - {self.student.name}"


class ProgressReport(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    feedback = models.TextField()
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.name} - {self.date}"


class LicenceTracking(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    application_date = models.DateField()
    test_date = models.DateField(null=True, blank=True)
    result = models.CharField(max_length=50, choices=[("Pending", "Pending"), ("Passed", "Passed"), ("Failed", "Failed")], default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.name} - {self.result}"


class DrivingTestHub(models.Model):
    location = models.CharField(max_length=100)
    examiner = models.CharField(max_length=100)
    test_date = models.DateField()
    slots_available = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.location} - {self.test_date}"


class SystemSetup(models.Model):
    setting_name = models.CharField(max_length=100)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.setting_name
