from django.db import models


class ContractType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContractTemplate(models.Model):
    name = models.CharField(max_length=200)
    template_file = models.FileField(upload_to='contract_templates/')
    contract_type = models.ForeignKey(ContractType, on_delete=models.CASCADE, related_name='templates')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Contract(models.Model):
    title = models.CharField(max_length=200)
    contract_type = models.ForeignKey(ContractType, on_delete=models.CASCADE, related_name='contracts')
    contract_template = models.ForeignKey(ContractTemplate, on_delete=models.CASCADE, related_name='contracts')
    start_date = models.DateField()
    end_date = models.DateField()
    parties_involved = models.CharField(max_length=500)  # Parties involved in the contract
    terms = models.TextField()  # Contract terms and conditions
    status = models.CharField(max_length=50, choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Terminated', 'Terminated')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
