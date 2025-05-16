from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.CharField(max_length=20, unique=True, editable=False)
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.customer_id:
            last = Customer.objects.order_by('id').last()
            next_id = last.id + 1 if last else 1
            self.customer_id = f"#CUST{str(next_id).zfill(6)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    vendor_id = models.CharField(max_length=20, unique=True, editable=False)
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.vendor_id:
            last = Vendor.objects.order_by('id').last()
            next_id = last.id + 1 if last else 1
            self.vendor_id = f"#VEND{str(next_id).zfill(6)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# Banking --------------------------------------------------------------

class BankAccount(models.Model):
    chart_of_account = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    bank = models.CharField(max_length=255)
    account_number = models.CharField(max_length=50)
    current_balance = models.DecimalField(max_digits=15, decimal_places=2)
    contact_number = models.CharField(max_length=20)
    bank_branch = models.CharField(max_length=255)
    swift = models.CharField(max_length=20, verbose_name='SWIFT Code')
    bank_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.bank}"

class ChartAccount(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('asset', 'Asset'),
        ('liability', 'Liability'),
        ('equity', 'Equity'),
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
    parent_account = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='sub_accounts')
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code} - {self.name}"
    

class Transfer(models.Model):
    from_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name='transfer_out')
    to_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name='transfer_in')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    reference = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Transfer {self.amount} from {self.from_account.name} to {self.to_account.name} on {self.created_at}"

class TransactionRecord(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
    ]

    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_name = models.CharField(max_length=255)
    transaction_amount = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.transaction_name} - {self.transaction_status}"

# Income      -------------------------------------------------------------------

class Revenue(models.Model):
    CATEGORY_CHOICES = [
        ('maintenancesales', 'MaintenanceSales'),
        ('productsales', 'ProductSales'),
    ]
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    reference = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.created_at.date()} - {self.amount} ({self.account})"

class CreditNotes(models.Model):
    STATUS_CHOICES = [
        ('fullyused', 'Fully Used'),
        ('partial', 'Partially Used'),
        ('pending', 'Pending'),
    ]

    invoice_number = models.CharField(max_length=20, unique=True, editable=False)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    updated_at =models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.invoice_number:
            last = CreditNotes.objects.order_by('id').last()
            next_id = last.id + 1 if last else 1
            self.invoice_number = f"#INV{str(next_id).zfill(6)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.invoice_number
    
# Expenses     ------------------------------------------------------------------------------

class BillRecord(models.Model):
    STATUS_CHOICES = [
        ('sent', 'Sent'),
        ('paid', 'Paid'),
        ('partialypaid', 'Partialy Paid'),
        ('draft', 'Draft'),
    ]

    ACCOUNT_TYPE_CHOICES = [
        ('projects', 'Projects'),
        ('accounting', 'Accounting'),
    ]

    bill_number = models.CharField(max_length=20, unique=True, editable=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
    bill_date = models.DateTimeField()
    due_date = models.DateTimeField()
    due_amount = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.bill_number:
            last = BillRecord.objects.order_by('id').last()
            next_id = last.id + 1 if last else 1
            self.bill_number = f"#BILL{str(next_id).zfill(6)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.bill_number

class PaymentRecord(models.Model):
    STATUS_CHOICES = [
        ('rentOrLease', 'Rent Or Lease'),
        ('travel', 'Travel'),
    ]
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=STATUS_CHOICES)
    reference = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vendor

class DebitNotes(models.Model):
    STATUS_CHOICES = [
        ('fullyused', 'Fully Used'),
        ('partial', 'Partially Used'),
        ('pending', 'Pending'),
    ]

    bill_number = models.CharField(max_length=20, unique=True, editable=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    updated_at =models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.bill_number:
            last = DebitNotes.objects.order_by('id').last()
            next_id = last.id + 1 if last else 1
            self.bill_number = f"#DBNT{str(next_id).zfill(6)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.bill_number

# Budget Planner     --------------------------------------------------------------------------

class Budget(models.Model):
    BUDGET_CHOICES = [
        ('monthly', 'monthly'),
        ('yearly', 'yearly'),
        ('half-yearly', 'half-yearly'),
        ('quarterly', 'quarterly'),
    ]
    name = models.CharField(max_length=255)
    from_date = models.DateTimeField()
    budget_period = models.CharField(max_length=20, choices=BUDGET_CHOICES, default='monthly')
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Financial Goal    --------------------------------------------------------------------------

class FinancialGoal(models.Model):
    goal_no = models.CharField(max_length=20, unique=True, editable=False)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    is_dashboard_display = models.BooleanField(default=False)
    updated_at =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.goal_no