from django.db import models
from UserMGMT.models import User


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    registered_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name



class Procurement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class RFx(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    procurement = models.ForeignKey(Procurement, on_delete=models.CASCADE, related_name="rfxs")
    created_at = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class RFxApplication(models.Model):
    rfx = models.ForeignKey(RFx, on_delete=models.CASCADE, related_name="applications")
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    submitted_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vendor.name} - {self.rfx.title}"



class RFxApplicant(models.Model):
    application = models.OneToOneField(RFxApplication, on_delete=models.CASCADE, related_name="applicant_details")
    contact_person = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Applicant: {self.contact_person}"



class RFxArchived(models.Model):
    original_rfx = models.OneToOneField(RFx, on_delete=models.CASCADE)
    archived_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Archived: {self.original_rfx.title}"



class VendorOnBoarding(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')])
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vendor.name} - {self.status}"



class RFxVendor(models.Model):
    rfx = models.ForeignKey(RFx, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    invited_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rfx.title} - {self.vendor.name}"


class CustomQuestion(models.Model):
    rfx = models.ForeignKey(RFx, on_delete=models.CASCADE, related_name="custom_questions")
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question



class InterviewSchedule(models.Model):
    application = models.ForeignKey(RFxApplication, on_delete=models.CASCADE, related_name="interviews")
    scheduled_on = models.DateTimeField()
    interviewer = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Interview for {self.application}"



class SystemSetup(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.key}: {self.value}"
