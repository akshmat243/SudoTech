from django.db import models
from django.utils import timezone


class VehicleSeller(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class VehicleBuyer(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    plate_number = models.CharField(max_length=20, unique=True)
    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.plate_number} - {self.model}"


class VehicleTrade(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    seller = models.ForeignKey(VehicleSeller, on_delete=models.CASCADE)
    buyer = models.ForeignKey(VehicleBuyer, on_delete=models.CASCADE)
    trade_date = models.DateField(default=timezone.now)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vehicle.plate_number} trade"


class PreviousServiceHistory(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    service_date = models.DateField()
    description = models.TextField()
    service_center = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vehicle.plate_number} - {self.service_date}"


class VehicleSpecification(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vehicle.plate_number} - {self.key}"


class VehicleCondition(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    condition = models.TextField()
    reported_on = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vehicle.plate_number} - condition"


class VehicleHistory(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    description = models.TextField()
    date_recorded = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vehicle.plate_number} - history"


class VehicleInsuranceHistory(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    provider = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=100)
    valid_from = models.DateField()
    valid_to = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vehicle.plate_number} - {self.policy_number}"


class Document(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vehicle.plate_number} - {self.name}"


class VehicleReport(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    report = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vehicle.plate_number} report"


class ExpertInspection(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    expert_name = models.CharField(max_length=100)
    inspection_date = models.DateField()
    findings = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vehicle.plate_number} inspected by {self.expert_name}"


class VehicleSetup(models.Model):
    key = models.CharField(max_length=100)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key
