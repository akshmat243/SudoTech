from rest_framework import serializers
from .models import *


class ReminderCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReminderCategory
        fields = '__all__'


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'
