from rest_framework import serializers
from .models import EmailBox, Email, EmailHistory
from UserMGMT.models import User

class EmailBoxSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Displaying user username as a string
    
    class Meta:
        model = EmailBox
        fields = '__all__'


class EmailSerializer(serializers.ModelSerializer):
    email_box = EmailBoxSerializer(read_only=True)
    sender = serializers.EmailField()
    recipient = serializers.EmailField()
    
    class Meta:
        model = Email
        fields = '__all__'


class EmailHistorySerializer(serializers.ModelSerializer):
    email = EmailSerializer(read_only=True)
    changed_by = serializers.StringRelatedField()  # Displaying user's username
    
    class Meta:
        model = EmailHistory
        fields = '__all__'
