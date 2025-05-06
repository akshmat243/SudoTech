from django.db import models
from datetime import timedelta

class Timesheet(models.Model):
    no = models.IntegerField()
    name = models.CharField(max_length=100)
    project = models.CharField(max_length=100)
    task = models.CharField(max_length=100)
    types = models.CharField(max_length=100)
    date = models.DateField()
    hours = models.IntegerField()
    minutes = models.IntegerField()
    total_time = models.DurationField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.total_time = timedelta(hours=self.hours, minutes=self.minutes)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.project} ({self.date})"
