from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
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
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HiveFilters
    
    def create(self, request, *args, **kwargs):
        beeyard_id = kwargs.get('beeyard_id')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(beeyard_id=beeyard_id)
        response = super().create(request, *args, **kwargs)
        return response
    
    def get_hives(self, request, *args, **kwargs):
        """" This function permits to send only the hives from a particular beeyard, defined in the url."""
        beeyard_id = kwargs.get('beeyard_id')
        beeyard=get_object_or_404(Beeyards, id=beeyard_id)
        hives = Hives.objects.filter(beeyard = beeyard)
        return render(request, 'hives.html', {'hives': hives, 'beeyard':beeyard})

