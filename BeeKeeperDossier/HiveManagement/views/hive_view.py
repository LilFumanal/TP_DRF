from django.http import HttpResponse
from django.shortcuts import render
from HiveManagement.models import Hives
from HiveManagement.serializers.hive_serializer import HiveSerializer
from rest_framework import permissions, viewsets, views
from django_filters import rest_framework as filters

class HiveFilters(filters.FilterSet):
    class Meta:
        model = Hives
        fields = {
            'id': {'exact'},
            'status': {'icontains', 'contains', 'exact'},
            'name': {'icontains', 'contains', 'exact'},
            'beeyard':{'exact'},
            'queen_age': {'exact'},
            'bee_type': {'icontains', 'contains', 'exact'}
        }
    
class HiveViewSet(viewsets.ModelViewSet):
    queryset = Hives.objects.all()
    serializer_class = HiveSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HiveFilters

def hive_template(request):
    hives = Hives.objects.all()
    return render(request, 'hive.html', {'hives': hives})