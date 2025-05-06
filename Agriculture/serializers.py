from rest_framework import serializers
from .models import (Agriculture, Fleet, Process, Equipment, Department, Office, Canal, ServiceProduct, Crop, User, Cultivation, Activity, Service, InventoryItem, Contract, Loan, PestDisease, WeatherData, SoilAnalysis, IrrigationSystem, ResearchDevelopment, ComplianceReport, SystemSetup
)

serializer_classes = {}
for model in [Agriculture, Fleet, Process, Equipment, Department, Office, Canal, ServiceProduct, Crop, User, Cultivation, Activity, Service, InventoryItem, Contract, Loan, PestDisease, WeatherData, SoilAnalysis, IrrigationSystem, ResearchDevelopment, ComplianceReport, SystemSetup
]:
    serializer_name = f"{model.__name__}Serializer"
    serializer_class = type(
        serializer_name,
        (serializers.ModelSerializer,),
        {
            "Meta": type("Meta", (), {"model": model, "fields": "__all__"})
        }
    )
    serializer_classes[serializer_name] = serializer_class