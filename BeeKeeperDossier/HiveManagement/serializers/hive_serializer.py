from HiveManagement.models import Hives
from rest_framework import serializers

class HiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hives
        fields = ['status','last_status_change', 'queen_age','bee_type','harvest','contamination']