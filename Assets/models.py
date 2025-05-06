from django.db import models

class Asset(models.Model):
    asset_tag = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    purchase_date = models.DateField()
    value = models.DecimalField(max_digits=12, decimal_places=2)
    location = models.CharField(max_length=255, blank=True, null=True)
    assigned_to = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive'), ('defective', 'Defective')])
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.asset_tag} - {self.name}"


class AssetHistory(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='histories')
    changed_by = models.CharField(max_length=100)
    change_type = models.CharField(max_length=100)  # e.g., "Transferred", "Status Update", etc.
    change_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.asset.asset_tag} - {self.change_type} on {self.change_date}"


class DefectiveAsset(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    reported_on = models.DateField()
    issue_description = models.TextField()
    resolved = models.BooleanField(default=False)
    resolution_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.asset.asset_tag} - Defective"


class AssetSystemSetup(models.Model):
    setting_name = models.CharField(max_length=255, unique=True)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.setting_name
