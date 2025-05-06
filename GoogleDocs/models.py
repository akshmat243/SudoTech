from django.db import models

class GoogleDoc(models.Model):
    title = models.CharField(max_length=255)
    doc_id = models.CharField(max_length=100, unique=True, help_text="The Google Docs unique document ID.")
    url = models.URLField(help_text="Public or shared Google Docs link.")
    owner_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_synced = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
