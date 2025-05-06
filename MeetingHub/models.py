from django.db import models
from UserMGMT.models import User

class MeetingType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Meeting(models.Model):
    meeting_type = models.ForeignKey(MeetingType, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=255, blank=True, null=True)
    attendees = models.ManyToManyField(User, related_name='meetings')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.subject} - {self.start_time}"

class MeetingMinutes(models.Model):
    meeting = models.OneToOneField(Meeting, on_delete=models.CASCADE, related_name='minutes')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Minutes for {self.meeting.subject}"

class MeetingReport(models.Model):
    meeting = models.OneToOneField(Meeting, on_delete=models.CASCADE, related_name='report')
    report_file = models.FileField(upload_to='media/meeting_reports/', blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.meeting.subject}"
