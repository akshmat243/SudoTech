from django.db import models
from django.utils import timezone


class Business(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="business_logos/", blank=True, null=True)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='contacts')
    full_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    linkedin = models.URLField(blank=True)
    added_on = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class Appointment(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='appointments')
    subject = models.CharField(max_length=255)
    scheduled_for = models.DateTimeField()
    location = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.subject} with {self.contact.full_name} at {self.scheduled_for.strftime('%Y-%m-%d %H:%M')}"
