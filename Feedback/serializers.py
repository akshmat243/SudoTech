from rest_framework import serializers
from .models import FeedbackTemplate, Feedback, FeedbackHistory
from UserMGMT.models import User


class FeedbackTemplateSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField() 

    class Meta:
        model = FeedbackTemplate
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    template = FeedbackTemplateSerializer(read_only=True) 
    user = serializers.StringRelatedField() 

    class Meta:
        model = Feedback
        fields = '__all__'


class FeedbackHistorySerializer(serializers.ModelSerializer):
    feedback = FeedbackSerializer(read_only=True) 
    updated_by = serializers.StringRelatedField()  

    class Meta:
        model = FeedbackHistory
        fields = '__all__'
