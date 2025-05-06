from rest_framework import serializers
from .models import (
    Account, Contact, Opportunity, Quote, SalesOrder, SalesInvoice, Case, 
    Stream, SalesDocument, Call, Meeting, SalesReport, SalesSystemSetup
)


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'


class OpportunitySerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)

    class Meta:
        model = Opportunity
        fields = '__all__'


class QuoteSerializer(serializers.ModelSerializer):
    opportunity = OpportunitySerializer(read_only=True)

    class Meta:
        model = Quote
        fields = '__all__'


class SalesOrderSerializer(serializers.ModelSerializer):
    quote = QuoteSerializer(read_only=True)

    class Meta:
        model = SalesOrder
        fields = '__all__'


class SalesInvoiceSerializer(serializers.ModelSerializer):
    sales_order = SalesOrderSerializer(read_only=True)

    class Meta:
        model = SalesInvoice
        fields = '__all__'


class CaseSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)

    class Meta:
        model = Case
        fields = '__all__'


class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stream
        fields = '__all__'


class SalesDocumentSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)

    class Meta:
        model = SalesDocument
        fields = '__all__'


class CallSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(read_only=True)

    class Meta:
        model = Call
        fields = '__all__'


class MeetingSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(read_only=True)

    class Meta:
        model = Meeting
        fields = '__all__'


class SalesReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesReport
        fields = '__all__'


class SalesSystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesSystemSetup
        fields = '__all__'
