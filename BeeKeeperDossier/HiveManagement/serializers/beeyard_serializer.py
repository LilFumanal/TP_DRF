from models import Beeyards
from rest_framework import serializers

class BeeyardSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="beekeeper.name", default=None, read_only=True)
    class Meta:
        model = Beeyards
        fields = ['name', 'user']