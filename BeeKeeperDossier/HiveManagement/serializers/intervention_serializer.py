from datetime import date
from HiveManagement.models import Intervention
from rest_framework import serializers

from HiveManagement.models.hives import Hives

class InterventionSerializer(serializers.ModelSerializer):
    hive = serializers.PrimaryKeyRelatedField(queryset=Hives.objects.all())
    class Meta:
        model = Intervention
        fields = ['hive', 'motif', 'date', 'harvest_quantity', 'is_sick', 'decease']
        extra_kwargs = {
            'hive': {'required': True},
        }