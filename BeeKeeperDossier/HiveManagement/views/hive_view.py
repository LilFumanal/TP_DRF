from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from HiveManagement.models import Hives, Beeyards
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
            'queen_age': {'exact'},
            'bee_type': {'icontains', 'contains', 'exact'}
        }
    
class HiveViewSet(viewsets.ModelViewSet):
    queryset = Hives.objects.all()
    serializer_class = HiveSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HiveFilters

def hive_template(request, beeyard_id):
    """" This function permits to send only the hives from a particular beeyard, defined in the url."""
    beeyard=get_object_or_404(Beeyards, id=beeyard_id)
    hives = Hives.objects.filter(beeyard = beeyard)
    return render(request, 'hive.html', {'hives': hives, 'beeyard':beeyard})