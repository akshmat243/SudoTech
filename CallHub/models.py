from django.db import models

class CallList(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CallHistory(models.Model):
    call_list = models.ForeignKey(CallList, on_delete=models.CASCADE, related_name='call_histories')
    contact_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    call_time = models.DateTimeField()
    duration = models.DurationField()
    status = models.CharField(max_length=50, choices=[('connected', 'Connected'), ('missed', 'Missed'), ('failed', 'Failed')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.contact_name} ({self.status})"


class Report(models.Model):
    call_list = models.ForeignKey(CallList, on_delete=models.CASCADE, related_name='reports')
    generated_on = models.DateTimeField(auto_now_add=True)
    total_calls = models.IntegerField()
    successful_calls = models.IntegerField()
    failed_calls = models.IntegerField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Report for {self.call_list.name} on {self.generated_on.date()}"


class SystemSetup(models.Model):
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.setting_name
