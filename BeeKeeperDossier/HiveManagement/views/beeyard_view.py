from django.http import HttpResponse
from django.shortcuts import render
from HiveManagement.models import Beeyards

from HiveManagement.serializers.beeyard_serializer import BeeyardSerializer
from rest_framework import permissions, viewsets, views
from django_filters import rest_framework as filters


class BeeyardFilters(filters.FilterSet):
    class Meta:
        #model = beeyard
        # fields = {
        #     'name': {'icontains', 'contains', 'exact'},
        #     'zone__name': {'icontains', 'contains', 'exact'},
        #     'zone__keepers__name': {'icontains', 'contains', 'exact'}
        # }
        pass
    
class BeeyardViewSet(viewsets.ModelViewSet):
    queryset = Beeyards.objects.all()
    serializer_class = BeeyardSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class =BeeyardFilters

def beeyard_template(request):
  return render(request, 'beeyard.html')