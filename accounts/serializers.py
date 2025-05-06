from rest_framework import serializers
from .models import (
    Customer, Vendor, BankAccount, ChartAccount, Transfer, TransactionRecord,
    Revenue, CreditNotes, BillRecord, PaymentRecord, DebitNotes, Budget, FinancialGoal
)

model_list = [
    Customer, Vendor, BankAccount, ChartAccount, Transfer, TransactionRecord,
    Revenue, CreditNotes, BillRecord, PaymentRecord, DebitNotes, Budget, FinancialGoal
]


serializer_classes = {}

for model in model_list:
    serializer_name = f"{model.__name__}Serializer"
    serializer_class = type(
        serializer_name,
        (serializers.ModelSerializer,),
        {
            "Meta": type("Meta", (), {"model": model, "fields": "__all__"})
        }
    )
    serializer_classes[serializer_name] = serializer_class


# serializer_classes['CustomerSerializer']
