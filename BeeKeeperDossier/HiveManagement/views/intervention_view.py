from django.http import HttpResponse
from django.shortcuts import render
from HiveManagement.models import Intervention
from HiveManagement.serializers.intervention_serializer import InterventionSerializer
from rest_framework import permissions, viewsets, views
from django_filters import rest_framework as filters


class InterventionFilters(filters.FilterSet):
    class Meta:
        #model = Intervention
        # fields = {
        #     'name': {'icontains', 'contains', 'exact'},
        #     'zone__name': {'icontains', 'contains', 'exact'},
        #     'zone__keepers__name': {'icontains', 'contains', 'exact'}
        # }
        pass
    
class InterventionViewSet(viewsets.ModelViewSet):
    queryset = Intervention.objects.all()
    serializer_class = InterventionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = InterventionFilters

def intervention_template(request):
  interventions = Intervention.objects.all()
  return render(request, 'interventions.html', {'interventions': interventions})