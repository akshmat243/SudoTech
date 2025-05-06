from django.db import models
from django.utils import timezone

class CollectionCenter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    manager_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class RawMaterial(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)
    quantity = models.FloatField()
    collection_center = models.ForeignKey(CollectionCenter, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Beverage(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    volume_ml = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class BillOfMaterial(models.Model):
    beverage = models.ForeignKey(Beverage, on_delete=models.CASCADE)
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    quantity_required = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.beverage.name} - {self.raw_material.name}"

class Manufacturing(models.Model):
    beverage = models.ForeignKey(Beverage, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    batch_number = models.CharField(max_length=100, unique=True)
    quantity_produced = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.beverage.name} - {self.batch_number}"

class Packaging(models.Model):
    manufacturing = models.ForeignKey(Manufacturing, on_delete=models.CASCADE)
    packaging_type = models.CharField(max_length=100)
    packaged_units = models.PositiveIntegerField()
    date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Packaged {self.packaged_units} units - {self.packaging_type}"

class QualityControl(models.Model):
    manufacturing = models.ForeignKey(Manufacturing, on_delete=models.CASCADE)
    tested_by = models.CharField(max_length=100)
    test_date = models.DateField(default=timezone.now)
    passed = models.BooleanField()
    remarks = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"QC - {self.manufacturing.beverage.name} - {'Pass' if self.passed else 'Fail'}"

class Maintenance(models.Model):
    equipment_name = models.CharField(max_length=100)
    last_maintenance_date = models.DateField()
    next_due_date = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.equipment_name

class WasteRecord(models.Model):
    manufacturing = models.ForeignKey(Manufacturing, on_delete=models.SET_NULL, null=True)
    waste_type = models.CharField(max_length=100)
    quantity = models.FloatField()
    date = models.DateField(default=timezone.now)
    reason = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.waste_type} - {self.quantity} units"
