from django.db import models
from django.utils import timezone

class Animal(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    health_status = models.CharField(max_length=100, blank=True, null=True)
    tag_number = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Animal {self.name} - {self.breed}"


class Health(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    health_status = models.CharField(max_length=255)
    date_recorded = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Health Record for {self.animal.name} on {self.date_recorded}"


class Breeding(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    breeding_date = models.DateField()
    breeding_partner = models.ForeignKey(Animal, related_name='breeding_partner', on_delete=models.SET_NULL, null=True)
    pregnancy_check_date = models.DateField(blank=True, null=True)
    is_pregnant = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Breeding Record for {self.animal.name} on {self.breeding_date}"


class Weight(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=8, decimal_places=2)
    date_recorded = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Weight Record for {self.animal.name} - {self.weight}kg"


class DailyMilkSheet(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    milk_quantity = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Milk Sheet for {self.animal.name} on {self.date}"


class MilkInventory(models.Model):
    milk_quantity = models.DecimalField(max_digits=8, decimal_places=2)
    date_added = models.DateTimeField(default=timezone.now)
    source = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Milk Inventory - {self.milk_quantity} Liters"


class CumulativeMilkSheet(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    total_milk = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cumulative Milk for {self.animal.name} from {self.start_date} to {self.end_date}"


class MilkProduct(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price_per_unit = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class FeedManagement(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    feed_type = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    feed_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Feed for {self.animal.name} - {self.feed_type}"


class Vaccination(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    vaccine_name = models.CharField(max_length=100)
    vaccination_date = models.DateField()
    next_vaccination_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Vaccination Record for {self.animal.name} - {self.vaccine_name}"


class SalesDistribution(models.Model):
    milk_product = models.ForeignKey(MilkProduct, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    sale_date = models.DateField()
    customer_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Sale of {self.milk_product.name} - {self.quantity} Liters"


class ExpenseTracking(models.Model):
    expense_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Expense {self.expense_type} - {self.amount}"


class CalvingBirthRecord(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    birth_date = models.DateField()
    birth_weight = models.DecimalField(max_digits=6, decimal_places=2)
    calf_gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Calving Record for {self.animal.name} - {self.birth_date}"


class EquipmentManagement(models.Model):
    equipment_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    purchase_date = models.DateField()
    maintenance_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.equipment_name
