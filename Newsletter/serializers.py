from rest_framework import serializers
from .models import Newsletter, Mail, MailHistory
from UserMGMT.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Adjust fields as needed


class NewsletterSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Newsletter
        fields = '__all__'


class MailSerializer(serializers.ModelSerializer):
    newsletter = NewsletterSerializer(read_only=True)

    class Meta:
        model = Mail
        fields = '__all__'


class MailHistorySerializer(serializers.ModelSerializer):
    mail = MailSerializer(read_only=True)
    status_changed_by = UserSerializer(read_only=True)

    class Meta:
        model = MailHistory
        fields = '__all__'
