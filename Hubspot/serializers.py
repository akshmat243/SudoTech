from rest_framework import serializers
from .models import HubSpotTicket


class HubSpotTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = HubSpotTicket
        fields = '__all__'
