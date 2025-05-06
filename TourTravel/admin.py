from django.contrib import admin
from .models import *

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'start_date', 'end_date', 'price_per_person']
    search_fields = ['name', 'location']
    list_filter = ['start_date', 'end_date']
    date_hierarchy = 'start_date'


@admin.register(TourBooking)
class TourBookingAdmin(admin.ModelAdmin):
    list_display = ['tour', 'customer_name', 'number_of_people', 'total_price', 'booking_date']
    search_fields = ['customer_name', 'tour__name']
    list_filter = ['booking_date']
    date_hierarchy = 'booking_date'


@admin.register(TouristInquiry)
class TouristInquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'inquiry_date']
    search_fields = ['name', 'email']
    date_hierarchy = 'inquiry_date'


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ['name', 'languages', 'phone', 'experience_years', 'available']
    list_filter = ['available']
    search_fields = ['name', 'languages']


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['title', 'discount_percentage', 'valid_from', 'valid_to']
    list_filter = ['valid_from', 'valid_to']
    date_hierarchy = 'valid_from'
    search_fields = ['title']


@admin.register(TravelInsurance)
class TravelInsuranceAdmin(admin.ModelAdmin):
    list_display = ['provider', 'cost', 'valid_from', 'valid_to']
    search_fields = ['provider']
    list_filter = ['valid_from', 'valid_to']
    date_hierarchy = 'valid_from'


@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ['setting_name']
    search_fields = ['setting_name']
