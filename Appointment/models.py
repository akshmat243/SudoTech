from django.db import models
from UserMGMT.models import User

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    appointment_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled')
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='Pending')

    def __str__(self):
        return f"{self.title} - {self.user.username} at {self.appointment_time}"

class Question(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=255)
    answer = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question: {self.question_text} (Appointment: {self.appointment.title})"

class Schedule(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='schedule')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"Schedule for {self.appointment.title} from {self.start_time} to {self.end_time}"

class AppointmentCallback(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='callback')
    callback_time = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    callback_status_choices = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled')
    ]
    callback_status = models.CharField(max_length=10, choices=callback_status_choices, default='Pending')

    def __str__(self):
        return f"Callback for {self.appointment.title} at {self.callback_time}"
