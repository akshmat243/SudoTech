from django.db import models
from django.utils import timezone

class Visitor(models.Model):
    full_name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    id_proof_type = models.CharField(max_length=100, blank=True)
    id_proof_number = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='visitor_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

class VisitorLog(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(null=True, blank=True)
    purpose = models.CharField(max_length=255)
    host_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.visitor.full_name} - {self.check_in.date()}"

class VisitorTimeline(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    note = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.visitor.full_name} - {self.timestamp}"

class VisitorBadge(models.Model):
    visitor_log = models.OneToOneField(VisitorLog, on_delete=models.CASCADE)
    badge_number = models.CharField(max_length=50)
    issued_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Badge {self.badge_number} - {self.visitor_log.visitor.full_name}"

class PreRegistration(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    scheduled_date = models.DateTimeField()
    host_name = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"PreReg: {self.visitor.full_name} on {self.scheduled_date}"

class VisitorDocument(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    document = models.FileField(upload_to='media/visitor_docs/')
    document_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.visitor.full_name} - {self.document_type}"

class VisitorCompliance(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    compliance_type = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.visitor.full_name} - {self.compliance_type}"

class VisitorIncident(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    incident_date = models.DateTimeField()
    description = models.TextField()
    reported_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Incident - {self.visitor.full_name} - {self.incident_date.date()}"

class VisitorReport(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='media/visitor_reports/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
