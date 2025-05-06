from django.db import models
from django.utils import timezone


class Site(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    manager = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Picking(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    material = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.material} - {self.site.name}"


class InternalPicking(models.Model):
    origin_site = models.ForeignKey(Site, related_name="origin_site", on_delete=models.CASCADE)
    destination_site = models.ForeignKey(Site, related_name="destination_site", on_delete=models.CASCADE)
    material = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    transfer_date = models.DateField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.material} from {self.origin_site} to {self.destination_site}"


class Inspection(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    inspector = models.CharField(max_length=100)
    date = models.DateField()
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.site.name} - {self.date}"


class Compliance(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    requirement = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[("Pending", "Pending"), ("Completed", "Completed")])
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.site.name} - {self.requirement}"


class Material(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    unit = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Scrap(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    material = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField()
    date_reported = models.DateField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.material} scrap at {self.site.name}"
