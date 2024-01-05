from HiveManagement.models import Intervention
from rest_framework import serializers

class InterventionSerializer(serializers.ModelSerializer):
    hive = serializers.CharField(source="hive.id", default=None, read_only=True)
    class Meta:
        model = Intervention
        fields = ['hive', 'motif', 'date']