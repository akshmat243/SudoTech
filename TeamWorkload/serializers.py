from rest_framework import serializers
from .models import TeamMember, Task, WorkloadOverview, WorkloadSettings

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    assigned_to = TeamMemberSerializer()

    class Meta:
        model = Task
        fields = '__all__'


class WorkloadOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkloadOverview
        fields = '__all__'


class WorkloadSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkloadSettings
        fields = '__all__'
