from django.db import models

class CourierAgent(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PendingCourier(models.Model):
    tracking_number = models.CharField(max_length=100, unique=True)
    sender_name = models.CharField(max_length=255)
    recipient_name = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Pending")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tracking_number


class Courier(models.Model):
    tracking_number = models.CharField(max_length=100, unique=True)
    agent = models.ForeignKey(CourierAgent, on_delete=models.SET_NULL, null=True)
    sender_name = models.CharField(max_length=255)
    recipient_name = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    dispatch_date = models.DateField()
    delivery_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[("Dispatched", "Dispatched"), ("In Transit", "In Transit"), ("Delivered", "Delivered"), ("Returned", "Returned")])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tracking_number


class Payment(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    method = models.CharField(max_length=50, choices=[("Cash", "Cash"), ("Card", "Card"), ("Bank Transfer", "Bank Transfer")])
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.courier.tracking_number} - {self.amount}"


class ServiceAgreement(models.Model):
    agent = models.ForeignKey(CourierAgent, on_delete=models.CASCADE)
    agreement_text = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Agreement with {self.agent.name}"


class CourierReturn(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    reason = models.TextField()
    return_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Return: {self.courier.tracking_number}"


class Contract(models.Model):
    party_name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.party_name


class SystemSetup(models.Model):
    key = models.CharField(max_length=255)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key
