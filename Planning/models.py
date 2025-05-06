from django.db import models

class Challenge(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Charter(models.Model):
    name = models.CharField(max_length=255)
    objective = models.TextField()
    stakeholders = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class BusinessPlan(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    goal = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class MarketingPlan(models.Model):
    campaign_name = models.CharField(max_length=255)
    target_market = models.TextField()
    strategy = models.TextField()
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.campaign_name


class BusinessModel(models.Model):
    model_name = models.CharField(max_length=255)
    description = models.TextField()
    revenue_streams = models.TextField()
    cost_structure = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model_name


class McKinsey7SModel(models.Model):
    shared_values = models.TextField()
    strategy = models.TextField()
    structure = models.TextField()
    systems = models.TextField()
    style = models.TextField()
    staff = models.TextField()
    skills = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"7-S Model {self.id}"


class PortersFiveForces(models.Model):
    threat_new_entrants = models.TextField()
    bargaining_power_buyers = models.TextField()
    threat_substitutes = models.TextField()
    bargaining_power_suppliers = models.TextField()
    industry_rivalry = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Porter's 5 Forces {self.id}"


class SWOTAnalysis(models.Model):
    strengths = models.TextField()
    weaknesses = models.TextField()
    opportunities = models.TextField()
    threats = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"SWOT {self.id}"


class PESTAnalysis(models.Model):
    political = models.TextField()
    economic = models.TextField()
    social = models.TextField()
    technological = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"PEST {self.id}"


class PESTELAnalysis(models.Model):
    political = models.TextField()
    economic = models.TextField()
    social = models.TextField()
    technological = models.TextField()
    environmental = models.TextField()
    legal = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"PESTEL {self.id}"


class PlanningSystemSetup(models.Model):
    config_name = models.CharField(max_length=255)
    config_value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.config_name
