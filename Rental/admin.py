from django.contrib import admin
from .models import Rental

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ['rental_number', 'customer', 'rental_type', 'start_date', 'end_date']
    list_filter = ['rental_type', 'start_date', 'end_date']
    search_fields = ['rental_number', 'customer']
