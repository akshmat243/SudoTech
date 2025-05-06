from django.db import models
from django.utils import timezone

RENTAL_TYPE_CHOICES = [
    ('Day', 'Day'),
    ('Week', 'Week'),
    ('Month', 'Month'),
]

class Rental(models.Model):
    rental_number = models.CharField(max_length=20, unique=True, default='#RENTALO000001')
    customer = models.CharField(max_length=100)
    rental_type = models.CharField(max_length=20, choices=RENTAL_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.rental_number

    def save(self, *args, **kwargs):
        if not self.rental_number or self.rental_number == '#RENTALO000001':
            last_rental = Rental.objects.all().order_by('id').last()
            if last_rental:
                last_id = int(last_rental.rental_number.replace('#RENTALO', ''))
                self.rental_number = f'#RENTALO{str(last_id + 1).zfill(6)}'
        super().save(*args, **kwargs)
