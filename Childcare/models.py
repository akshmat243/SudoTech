from django.db import models
from django.utils import timezone


class Parent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Inquiry(models.Model):
    parent_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return f"Inquiry from {self.parent_name}"


class Child(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    enrolled_date = models.DateField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name


class Attendance(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[("Present", "Present"), ("Absent", "Absent")])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.child} - {self.date} - {self.status}"


class ParentCommunication(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    message = models.TextField()
    date_sent = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"To {self.parent.name} on {self.date_sent}"


class DailyReport(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    date = models.DateField()
    activities = models.TextField()
    meals = models.TextField()
    nap_time = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.child.name} - {self.date}"


class BehavioralRecord(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    date = models.DateField()
    behavior_note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.child.name} - {self.date}"


class LearningOutcome(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    date = models.DateField()
    milestone = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.child.name} - {self.milestone}"


class SystemSetup(models.Model):
    setting_name = models.CharField(max_length=100)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.setting_name
