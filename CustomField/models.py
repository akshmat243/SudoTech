from django.db import models

class CustomField(models.Model):
    FIELD_TYPES = [
        ('text', 'Text'),
        ('number', 'Number'),
        ('date', 'Date'),
        ('boolean', 'Boolean'),
        ('select', 'Select'),
    ]

    name = models.CharField(max_length=100)
    field_type = models.CharField(max_length=20, choices=FIELD_TYPES)
    module = models.CharField(max_length=100, help_text="The name of the module this field is associated with.")
    rule = models.TextField(blank=True, help_text="Validation rule or condition for this custom field.")

    def __str__(self):
        return f"{self.name} ({self.module})"
