from rest_framework import serializers
from .models import DocumentType, DocumentTemplate, Document


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = '__all__'


class DocumentTemplateSerializer(serializers.ModelSerializer):
    document_type = DocumentTypeSerializer(read_only=True)

    class Meta:
        model = DocumentTemplate
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    document_type = DocumentTypeSerializer(read_only=True)
    document_template = DocumentTemplateSerializer(read_only=True)

    class Meta:
        model = Document
        fields = '__all__'
