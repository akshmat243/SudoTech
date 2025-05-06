from django.db import models

class Request(models.Model):
    REQUEST_TYPE_CHOICES = [
        ('support', 'Support'),
        ('service', 'Service'),
        ('inquiry', 'Inquiry'),
        ('feedback', 'Feedback'),
    ]

    request_id = models.CharField(max_length=100, unique=True)
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPE_CHOICES)
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[('open', 'Open'), ('closed', 'Closed'), ('in-progress', 'In Progress')], default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"Request {self.request_id} - {self.request_type} by {self.customer_name}"


class RequestSystemSetup(models.Model):
    setting_name = models.CharField(max_length=255, unique=True)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.setting_name
