from datetime import date
from django.http import HttpResponse
from django.shortcuts import render
from HiveManagement.models import Intervention, Beeyards, Hives
from HiveManagement.serializers.intervention_serializer import InterventionSerializer
from rest_framework import permissions, viewsets, views
from rest_framework.decorators import action
from django_filters import rest_framework as filters


class InterventionFilters(filters.FilterSet):
    class Meta:
        model = Intervention
        fields = {
            'motif': {'exact'},
            'hive': {'exact'},
            'date': {'contains', 'exact'},
            'harvest_quantity': {'contains', 'exact'},
            'is_sick': {'exact'},
            'decease': {'contains', 'exact'}
        }
    
class InterventionViewSet(viewsets.ModelViewSet):
    queryset = Intervention.objects.all()
    serializer_class = InterventionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = InterventionFilters
    
    
    @action(detail=True, methods=["POST"])
    def on_intervention(self, request):
        """ This function will change the status of the concerned hive if it's destroyed, and always update the date of the last change."""
        hive = request.data.get('hive_id')
        if request.data.get('motif') == "Dest":
            hive.status = "X"
        hive.last_status_changed = date.today()
        hive.save()


def intervention_template(request):
    """ This function will send only the interventions on beeyard owned by the user."""
    user_id = request.user.id
    beeyard = Beeyards.objects.filter(user__id=user_id)
    hives = Hives.objects.filter(beeyard__in=beeyard)
    interventions = Intervention.objects.filter(hive__in=hives)
    return render(request , 'interventions.html', {'interventions': interventions})


