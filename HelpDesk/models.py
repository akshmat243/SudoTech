from django.db import models
from UserMGMT.models import User

class HelpdeskCategory(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class HelpdeskTicket(models.Model):
    ticket_no = models.CharField(max_length=20, unique=True)
    subject = models.CharField(max_length=255)
    email = models.EmailField()
    created_by = models.ForeignKey(User, related_name='created_tickets', on_delete=models.SET_NULL, null=True, blank=True)
    assigned_to = models.ForeignKey(User, related_name='assigned_tickets', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(HelpdeskCategory, on_delete=models.SET_NULL, null=True, blank=True)
    
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ticket_no} - {self.subject}"
