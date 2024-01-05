from models import Hives
from rest_framework import serializers

class HiveSerializer(serializers.ModelSerializer):
    zone_name = serializers.CharField(source="zone.name", default=None, read_only=True)
    class Meta:
        model = Hives
        fields = ['status','last_status_change', 'queen_age','bee_type','harvest','contamination']