from rest_framework import serializers
from .models import Workflow, TaskStatus, Task
from UserMGMT.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # adjust fields as needed


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    status = TaskStatusSerializer(read_only=True)
    assigned_to = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'


class WorkflowSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Workflow
        fields = '__all__'
