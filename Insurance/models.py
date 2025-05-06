from django.db import models

class PolicyType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class InsurancePolicy(models.Model):
    policy_number = models.CharField(max_length=100, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    policy_type = models.ForeignKey(PolicyType, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[("Active", "Active"), ("Expired", "Expired"), ("Cancelled", "Cancelled")])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.policy_number


class Invoice(models.Model):
    policy = models.ForeignKey(InsurancePolicy, on_delete=models.CASCADE)
    issue_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Invoice {self.id} - {self.policy.policy_number}"


class Claim(models.Model):
    policy = models.ForeignKey(InsurancePolicy, on_delete=models.CASCADE)
    claim_date = models.DateField()
    claim_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[("Pending", "Pending"), ("Approved", "Approved"), ("Rejected", "Rejected")])
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Claim {self.id} - {self.status}"


class RiskAssessment(models.Model):
    policy = models.ForeignKey(InsurancePolicy, on_delete=models.CASCADE)
    assessment_date = models.DateField()
    risk_level = models.CharField(max_length=50, choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")])
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.policy.policy_number} - {self.risk_level}"


class Reinsurance(models.Model):
    policy = models.ForeignKey(InsurancePolicy, on_delete=models.CASCADE)
    reinsurance_company = models.CharField(max_length=255)
    coverage_percentage = models.FloatField()
    agreement_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.reinsurance_company} - {self.policy.policy_number}"


class UnderwritingRequest(models.Model):
    policy = models.ForeignKey(InsurancePolicy, on_delete=models.CASCADE)
    request_date = models.DateField()
    status = models.CharField(max_length=50, choices=[("Open", "Open"), ("Reviewed", "Reviewed"), ("Closed", "Closed")])
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"UW Request - {self.policy.policy_number}"


class Compliance(models.Model):
    policy = models.ForeignKey(InsurancePolicy, on_delete=models.CASCADE)
    compliance_check_date = models.DateField()
    compliant = models.BooleanField()
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.policy.policy_number} - {'Compliant' if self.compliant else 'Non-compliant'}"


class CustomerSupport(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    issue = models.TextField()
    status = models.CharField(max_length=50, choices=[("Open", "Open"), ("In Progress", "In Progress"), ("Resolved", "Resolved")])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Support - {self.customer.full_name}"


class MarketingCampaign(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    result_summary = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class FraudDetection(models.Model):
    policy = models.ForeignKey(InsurancePolicy, on_delete=models.CASCADE)
    flagged_date = models.DateField()
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[("Under Review", "Under Review"), ("Cleared", "Cleared"), ("Fraud Confirmed", "Fraud Confirmed")])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.policy.policy_number} - {self.status}"


class SystemSetup(models.Model):
    setting_name = models.CharField(max_length=255)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.setting_name
