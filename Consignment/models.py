from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Consignment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_received = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, choices=[('received', 'Received'), ('pending', 'Pending'), ('dispatched', 'Dispatched')], default='pending')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Consignment of {self.product.name} - {self.status}"


class PurchaseOrder(models.Model):
    supplier_name = models.CharField(max_length=255)
    order_date = models.DateTimeField(default=timezone.now)
    products = models.ManyToManyField(Product, through='PurchaseOrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Purchase Order from {self.supplier_name} on {self.order_date}"

class PurchaseOrderItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"


class SaleOrder(models.Model):
    customer_name = models.CharField(max_length=255)
    order_date = models.DateTimeField(default=timezone.now)
    products = models.ManyToManyField(Product, through='SaleOrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Sale Order for {self.customer_name} on {self.order_date}"

class SaleOrderItem(models.Model):
    sale_order = models.ForeignKey(SaleOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"


class Shipping(models.Model):
    sale_order = models.ForeignKey(SaleOrder, on_delete=models.CASCADE)
    shipping_address = models.TextField()
    shipping_date = models.DateTimeField(default=timezone.now)
    tracking_number = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Shipping for {self.sale_order.customer_name} - {self.tracking_number}"


class Returns(models.Model):
    sale_order = models.ForeignKey(SaleOrder, on_delete=models.CASCADE)
    return_reason = models.TextField()
    return_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, choices=[('requested', 'Requested'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='requested')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Return for {self.sale_order.customer_name} - {self.status}"


class QualityControl(models.Model):
    consignment = models.ForeignKey(Consignment, on_delete=models.CASCADE)
    inspection_date = models.DateTimeField(default=timezone.now)
    inspector_name = models.CharField(max_length=255)
    inspection_report = models.TextField()
    status = models.CharField(max_length=50, choices=[('approved', 'Approved'), ('rejected', 'Rejected')], default='approved')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Quality Control for {self.consignment.product.name} - {self.status}"


class Contract(models.Model):
    consignment = models.ForeignKey(Consignment, on_delete=models.CASCADE)
    contract_number = models.CharField(max_length=255)
    contract_date = models.DateTimeField(default=timezone.now)
    terms_and_conditions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Contract {self.contract_number} for {self.consignment.product.name}"


class Compliance(models.Model):
    consignment = models.ForeignKey(Consignment, on_delete=models.CASCADE)
    compliance_document = models.FileField(upload_to='compliance_documents/')
    compliance_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, choices=[('compliant', 'Compliant'), ('non-compliant', 'Non-Compliant')], default='compliant')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Compliance for {self.consignment.product.name} - {self.status}"
