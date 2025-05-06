from django.db import models
from UserMGMT.models import User

class FeedbackTemplate(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_templates')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    template = models.ForeignKey(FeedbackTemplate, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='feedback_given')
    content = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.user} on {self.submitted_at}"


class FeedbackHistory(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    old_content = models.TextField()

    def __str__(self):
        return f"History for {self.feedback.id} at {self.updated_at}"
