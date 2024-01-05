from models import Beekeepers
from rest_framework import serializers

class BeekeeperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beekeepers
        fields = ['email', 'username', 'name', 'surname']