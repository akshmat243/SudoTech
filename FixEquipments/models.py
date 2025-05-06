from django.db import models


class FixEquipment(models.Model):
    EQUIPMENT_TYPE_CHOICES = [
        ('asset', 'Asset'),
        ('license', 'License'),
        ('accessory', 'Accessory'),
        ('consumable', 'Consumable'),
        ('component', 'Component'),
        ('kit', 'Pre Defined Kit'),
    ]

    equipment_id = models.CharField(max_length=100, unique=True)
    equipment_type = models.CharField(max_length=50, choices=EQUIPMENT_TYPE_CHOICES)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    purchase_date = models.DateField()
    value = models.DecimalField(max_digits=12, decimal_places=2)
    location = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    assigned_to = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.equipment_id})"



class EquipmentMaintenance(models.Model):
    equipment = models.ForeignKey(FixEquipment, on_delete=models.CASCADE)
    maintenance_date = models.DateField()
    maintenance_type = models.CharField(max_length=100)  # e.g., "Routine", "Repair", etc.
    description = models.TextField(blank=True, null=True)
    next_service_due = models.DateField()
    status = models.CharField(max_length=50, choices=[('completed', 'Completed'), ('pending', 'Pending')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Maintenance for {self.equipment.name} on {self.maintenance_date}"


class EquipmentAudit(models.Model):
    equipment = models.ForeignKey(FixEquipment, on_delete=models.CASCADE)
    audit_date = models.DateField()
    auditor_name = models.CharField(max_length=255)
    findings = models.TextField()
    audit_status = models.CharField(max_length=50, choices=[('compliant', 'Compliant'), ('non-compliant', 'Non-Compliant')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Audit for {self.equipment.name} on {self.audit_date}"



class EquipmentSystemSetup(models.Model):
    setting_name = models.CharField(max_length=255, unique=True)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.setting_name
