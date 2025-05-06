from django.db import models

class GoogleLead(models.Model):
    lead_no = models.CharField(max_length=50, unique=True, verbose_name="No")
    name = models.CharField(max_length=255)
    keywords = models.TextField(help_text="Comma-separated keywords", blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    contacts_found = models.PositiveIntegerField(default=0, verbose_name="Contacts Found")

    def __str__(self):
        return f"{self.lead_no} - {self.name}"
