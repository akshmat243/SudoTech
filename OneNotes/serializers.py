from rest_framework import serializers
from .models import OneNoteNotebook, OneNoteSection, OneNotePage


class OneNotePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OneNotePage
        fields = '__all__'


class OneNoteSectionSerializer(serializers.ModelSerializer):
    pages = OneNotePageSerializer(many=True, read_only=True)

    class Meta:
        model = OneNoteSection
        fields = '__all__'


class OneNoteNotebookSerializer(serializers.ModelSerializer):
    sections = OneNoteSectionSerializer(many=True, read_only=True)

    class Meta:
        model = OneNoteNotebook
        fields = '__all__'
