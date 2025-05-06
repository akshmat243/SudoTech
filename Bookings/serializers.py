from rest_framework import serializers
from .models import (Customer, Staff, Item, Package, Appointment, Booking, SystemSetup)

serializer_classes = {}

for model in [Customer, Staff, Item, Package, Appointment, Booking, SystemSetup]:
    serializer_name = f"{model.__name__}Serializer"
    serializer_class = type(
        serializer_name,
        (serializers.ModelSerializer,),
        {
            "Meta": type("Meta", (), {"model": model, "fields": "__all__"})
        }
    )
    serializer_classes[serializer_name] = serializer_class
