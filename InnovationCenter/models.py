from django.db import models

class UpcomingChallenge(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class NewCreativity(models.Model):
    name = models.CharField(max_length=255)
    idea_summary = models.TextField()
    submitted_by = models.CharField(max_length=255)
    submitted_on = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class InnovationSystemSetup(models.Model):
    config_name = models.CharField(max_length=255)
    config_value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.config_name
