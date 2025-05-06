from rest_framework import serializers
from .models import File, Activity, Trash, FileVerification
from UserMGMT.models import User


class FileSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()  
    uploaded_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S") 

    class Meta:
        model = File
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    file = FileSerializer(read_only=True) 
    user = serializers.StringRelatedField() 

    class Meta:
        model = Activity
        fields = '__all__'


class TrashSerializer(serializers.ModelSerializer):
    file = FileSerializer(read_only=True)  
    trashed_by = serializers.StringRelatedField()  

    class Meta:
        model = Trash
        fields = '__all__'


class FileVerificationSerializer(serializers.ModelSerializer):
    file = FileSerializer(read_only=True) 
    verifier = serializers.StringRelatedField()  

    class Meta:
        model = FileVerification
        fields = '__all__'
