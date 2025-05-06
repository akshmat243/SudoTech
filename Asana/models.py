from django.db import models

class AsanaWorkspace(models.Model):
    workspace_id = models.CharField(max_length=100, unique=True)
    workspace_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.workspace_name} ({self.workspace_id})"
