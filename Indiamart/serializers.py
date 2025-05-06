from rest_framework import serializers
from .models import IndiaMartInquiry


class IndiaMartInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = IndiaMartInquiry
        fields = '__all__'
