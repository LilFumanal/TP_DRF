from HiveManagement.models import Beeyards
from rest_framework import serializers

class BeeyardSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="User.name", default=None, read_only=True)
    class Meta:
        model = Beeyards
        fields = ['name', 'user_name']