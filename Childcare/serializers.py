from rest_framework import serializers
from .models import (Parent, Inquiry, Child, Attendance, ParentCommunication, DailyReport, BehavioralRecord, LearningOutcome, SystemSetup)

serializer_classes = {}

for model in [Parent, Inquiry, Child, Attendance, ParentCommunication, DailyReport, BehavioralRecord, LearningOutcome, SystemSetup]:
    serializer_name = f"{model.__name__}Serializer"
    serializer_class = type(
        serializer_name,
        (serializers.ModelSerializer,),
        {
            "Meta": type("Meta", (), {"model": model, "fields": "__all__"})
        }
    )
    serializer_classes[serializer_name] = serializer_class
