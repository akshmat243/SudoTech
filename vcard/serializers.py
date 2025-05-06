from rest_framework import serializers
from .models import Business, Contact, Appointment


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('id', 'name', 'logo', 'website', 'phone', 'email', 'address', 'created_at', 'updated_at')


class ContactSerializer(serializers.ModelSerializer):
    business = BusinessSerializer()

    class Meta:
        model = Contact
        fields = ('id', 'business', 'full_name', 'title', 'email', 'phone', 'linkedin', 'added_on', 'updated_at')


class AppointmentSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()

    class Meta:
        model = Appointment
        fields = ('id', 'contact', 'subject', 'scheduled_for', 'location', 'notes', 'created_at', 'updated_at')
