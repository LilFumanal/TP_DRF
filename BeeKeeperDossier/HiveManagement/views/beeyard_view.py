from django.http import HttpResponse
from django.shortcuts import render
from HiveManagement.models import Beeyards

from HiveManagement.serializers.beeyard_serializer import BeeyardSerializer
from rest_framework import permissions, viewsets, views
from django_filters import rest_framework as filters


class BeeyardFilters(filters.FilterSet):
    class Meta:
        model = Beeyards
        fields = {
            'name': {'icontains', 'contains', 'exact'},
            'user__username': {'icontains', 'contains', 'exact'}
        }
    
class BeeyardViewSet(viewsets.ModelViewSet):
    queryset = Beeyards.objects.all()
    serializer_class = BeeyardSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class =BeeyardFilters

def beeyard_template(request):
    user_id = request.user.id
    beeyards = Beeyards.objects.filter(user__id=user_id)
    return render(request, 'beeyards.html', {"beeyards": beeyards})