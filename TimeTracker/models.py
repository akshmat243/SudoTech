from django.db import models
from datetime import datetime, timedelta

class Timetracker(models.Model):
    description = models.CharField(max_length=100)
    project = models.CharField(max_length=100)
    task = models.CharField(max_length=100)
    workspace = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    total_time = models.DurationField(blank=True, null=True)  # use DurationField for accuracy

    def save(self, *args, **kwargs):
        # Convert times to datetime for calculation
        if self.start_time and self.end_time:
            start_dt = datetime.combine(datetime.today(), self.start_time)
            end_dt = datetime.combine(datetime.today(), self.end_time)
            if end_dt < start_dt:
                end_dt += timedelta(days=1)
            self.total_time = end_dt - start_dt
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.project} - {self.task}"
