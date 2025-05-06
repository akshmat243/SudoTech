from rest_framework import serializers
from .models import Visitor, VisitorLog, VisitorTimeline, VisitorBadge, PreRegistration, VisitorDocument, VisitorCompliance, VisitorIncident, VisitorReport


class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ('id', 'full_name', 'company', 'email', 'phone', 'id_proof_type', 'id_proof_number', 'photo', 'created_at', 'updated_at')


class VisitorLogSerializer(serializers.ModelSerializer):
    visitor = VisitorSerializer()

    class Meta:
        model = VisitorLog
        fields = ('id', 'visitor', 'check_in', 'check_out', 'purpose', 'host_name', 'location', 'created_at', 'updated_at')


class VisitorTimelineSerializer(serializers.ModelSerializer):
    visitor = VisitorSerializer()

    class Meta:
        model = VisitorTimeline
        fields = ('id', 'visitor', 'timestamp', 'note', 'updated_at')


class VisitorBadgeSerializer(serializers.ModelSerializer):
    visitor_log = VisitorLogSerializer()

    class Meta:
        model = VisitorBadge
        fields = ('id', 'visitor_log', 'badge_number', 'issued_at', 'returned_at', 'updated_at')


class PreRegistrationSerializer(serializers.ModelSerializer):
    visitor = VisitorSerializer()

    class Meta:
        model = PreRegistration
        fields = ('id', 'visitor', 'scheduled_date', 'host_name', 'purpose', 'created_at', 'updated_at')


class VisitorDocumentSerializer(serializers.ModelSerializer):
    visitor = VisitorSerializer()

    class Meta:
        model = VisitorDocument
        fields = ('id', 'visitor', 'document', 'document_type', 'created_at', 'updated_at')


class VisitorComplianceSerializer(serializers.ModelSerializer):
    visitor = VisitorSerializer()

    class Meta:
        model = VisitorCompliance
        fields = ('id', 'visitor', 'compliance_type', 'status', 'note', 'created_at', 'updated_at')


class VisitorIncidentSerializer(serializers.ModelSerializer):
    visitor = VisitorSerializer()

    class Meta:
        model = VisitorIncident
        fields = ('id', 'visitor', 'incident_date', 'description', 'reported_by', 'created_at', 'updated_at')


class VisitorReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorReport
        fields = ('id', 'title', 'created_at', 'file', 'updated_at')
