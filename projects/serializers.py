from rest_framework import serializers
from .models import Project, ProjectTemplate, ProjectReport
from UserMGMT.models import User

class ProjectSerializer(serializers.ModelSerializer):
    assigned_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Project
        fields = '__all__'


class ProjectTemplateSerializer(serializers.ModelSerializer):
    assigned_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = ProjectTemplate
        fields = '__all__'


class ProjectReportSerializer(serializers.ModelSerializer):
    project_members = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = ProjectReport
        fields = '__all__'
