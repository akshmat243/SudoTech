from django.db import models

class ElderlyResident(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    medical_conditions = models.TextField(blank=True)
    emergency_contact = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Caretaker(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    assigned_resident = models.ForeignKey(ElderlyResident, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CareRequest(models.Model):
    resident = models.ForeignKey(ElderlyResident, on_delete=models.CASCADE)
    request_date = models.DateField(auto_now_add=True)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[("Pending", "Pending"), ("In Progress", "In Progress"), ("Completed", "Completed")], default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Request by {self.resident.name} on {self.request_date}"


class DailyActivitySchedule(models.Model):
    resident = models.ForeignKey(ElderlyResident, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=255)
    time = models.TimeField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.activity_name} for {self.resident.name}"


class HealthCheckup(models.Model):
    resident = models.ForeignKey(ElderlyResident, on_delete=models.CASCADE)
    checkup_date = models.DateField()
    vitals = models.TextField()
    doctor_notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Health Check - {self.resident.name} on {self.checkup_date}"


class MealPlan(models.Model):
    resident = models.ForeignKey(ElderlyResident, on_delete=models.CASCADE)
    date = models.DateField()
    breakfast = models.CharField(max_length=255)
    lunch = models.CharField(max_length=255)
    dinner = models.CharField(max_length=255)
    snacks = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Meal Plan for {self.resident.name} on {self.date}"
