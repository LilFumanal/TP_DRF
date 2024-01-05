from django.contrib.auth.models import User
from rest_framework import serializers

class BeekeeperSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'name', 'surname']