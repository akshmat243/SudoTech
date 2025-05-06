from rest_framework import serializers
from .models import SendinblueMail, SendinblueTemplate, SendinblueContact


class SendinblueMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendinblueMail
        fields = '__all__'


class SendinblueTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendinblueTemplate
        fields = '__all__'


class SendinblueContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendinblueContact
        fields = '__all__'
