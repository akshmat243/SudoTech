from rest_framework import serializers
from .models import (AsanaWorkspace)

for model in [AsanaWorkspace]:
    class AsanaWorkspaceSerializer(serializers.ModelSerializer):
        class Meta:
            model = model
            fields = '__all__'
