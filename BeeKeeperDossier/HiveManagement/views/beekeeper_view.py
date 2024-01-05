from django.http import HttpResponse
from django.shortcuts import render

from HiveManagement.serializers.beekeeper_serializer import BeekeeperSerializer
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets, views
from django_filters import rest_framework as filters

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = BeekeeperSerializer
    permission_classes = [permissions.IsAuthenticated]