from rest_framework import serializers
from .models import JobOpening, Applicant

class JobOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOpening
        fields = '__all__'


class ApplicantSerializer(serializers.ModelSerializer):
    job = JobOpeningSerializer()

    class Meta:
        model = Applicant
        fields = '__all__'
