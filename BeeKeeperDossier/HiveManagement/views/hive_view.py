from django.http import HttpResponse
from django.shortcuts import render
from models import Hives
from serializers.hive_serializer import HiveSerializer
from rest_framework import permissions, viewsets, views
from django_filters import rest_framework as filters

def hive_template(request):
  return render(request, 'hive.html')

class HiveFilters(filters.FilterSet):
    class Meta:
        model = Hives
        # fields = {
        #     'name': {'icontains', 'contains', 'exact'},
        #     'zone__name': {'icontains', 'contains', 'exact'},
        #     'zone__keepers__name': {'icontains', 'contains', 'exact'}
        # }
    
class HiveViewSet(viewsets.ModelViewSet):
    queryset = Hives.objects.all()
    serializer_class = HiveSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HiveFilters