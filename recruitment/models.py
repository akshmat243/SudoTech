from django.db import models

class JobOpening(models.Model):
    JOB_TYPE_CHOICES = [
        ('full-time', 'Full-Time'),
        ('part-time', 'Part-Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
    ]

    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('paused', 'Paused'),
    ]

    title = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    description = models.TextField()
    requirements = models.TextField()
    salary_range = models.CharField(max_length=100, blank=True)
    posted_date = models.DateField(auto_now_add=True)
    closing_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return f"{self.title} ({self.department})"


class Applicant(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('screening', 'Screening'),
        ('interviewed', 'Interviewed'),
        ('offered', 'Offered'),
        ('hired', 'Hired'),
        ('rejected', 'Rejected'),
    ]

    job = models.ForeignKey(JobOpening, on_delete=models.CASCADE, related_name='applicants')
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    resume = models.FileField(upload_to='applicant_resumes/')
    cover_letter = models.TextField(blank=True)
    application_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='applied')
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} - {self.job.title}"
