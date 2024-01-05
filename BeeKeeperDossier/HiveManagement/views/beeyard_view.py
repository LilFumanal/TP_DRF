from django.http import HttpResponse
from django.shortcuts import render

from models import Beeyards
from serializers.beeyard_serializer import BeeyardSerializer
from rest_framework import permissions, viewsets, views
from django_filters import rest_framework as filters


class BeeyardFilters(filters.FilterSet):
    class Meta:
        model = Beeyards
        # fields = {
        #     'name': {'icontains', 'contains', 'exact'},
        #     'zone__name': {'icontains', 'contains', 'exact'},
        #     'zone__keepers__name': {'icontains', 'contains', 'exact'}
        # }
    
class BeeyardViewSet(viewsets.ModelViewSet):
    queryset = Beeyards.objects.all()
    serializer_class = BeeyardSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class =BeeyardFilters

def beeyard_template(request):
  return render(request, 'beeyard.html')