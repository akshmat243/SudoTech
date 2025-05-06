from django.db import models


class FormEntry(models.Model):
    no = models.PositiveIntegerField("No")
    name = models.CharField("Name", max_length=255)
    response = models.TextField("Response")

    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.no}. {self.name}"
