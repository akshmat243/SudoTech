from django.db import models
from django.utils import timezone

class Ticket(models.Model):
    ticket_number = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    description = models.TextField()
    priority_choices = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ]
    priority = models.CharField(max_length=10, choices=priority_choices, default='medium')
    status_choices = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed')
    ]
    status = models.CharField(max_length=15, choices=status_choices, default='open')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ticket #{self.ticket_number} - {self.subject}"

class KnowledgeBase(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"FAQ - {self.question}"

class SystemSetup(models.Model):
    setting_name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.setting_name
