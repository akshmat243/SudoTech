from django.db import models

class PropertyManage(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Property(models.Model):
    manager = models.ForeignKey(PropertyManage, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    unit_number = models.CharField(max_length=50)
    size_sqft = models.FloatField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.property.name} - {self.unit_number}"


class Listing(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    listed_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Listing - {self.unit}"


class Tenant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Invoice #{self.id} for {self.tenant.name}"


class MaintenanceRequest(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[("Pending", "Pending"), ("In Progress", "In Progress"), ("Resolved", "Resolved")])
    request_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Maintenance - {self.unit}"


class DocumentType(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TenantRequest(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Request from {self.tenant.name}"


class ExpenseTracking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.property.name} - {self.category}"


class Inspection(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    inspector_name = models.CharField(max_length=255)
    inspection_date = models.DateField()
    remarks = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Inspection - {self.unit}"


class TenantCommunication(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"To: {self.tenant.name} - {self.subject}"


class Utility(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)  # e.g., Water, Electricity
    reading = models.FloatField()
    bill_amount = models.DecimalField(max_digits=10, decimal_places=2)
    billing_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.unit} - {self.type}"


class Contractor(models.Model):
    name = models.CharField(max_length=255)
    service_type = models.CharField(max_length=100)
    contact_info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
