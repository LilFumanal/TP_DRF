from datetime import date
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render, redirect
from django.db import transaction
from HiveManagement.models import Intervention, Beeyards, Hives
from HiveManagement.serializers.intervention_serializer import InterventionSerializer
from rest_framework import permissions, viewsets
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
    
    def create(self, request, *args, **kwargs):
        # Ajoutez ici votre logique pour mettre à jour la ruche avant de créer l'intervention
        hive_id = request.data.get('hive')
        intervention_motif = request.data.get('motif')
        hive = get_object_or_404(Hives, id=hive_id)
        request.data['date'] = date.today()

        with transaction.atomic():
            if intervention_motif == "Dest":
                hive.status = "X"
            hive.last_status_change = date.today()
            hive.save()
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['hive'] = hive
            response = super().create(request, *args, **kwargs)

        return redirect('interventions')

def intervention_template(request):
    """ This function will send only the interventions on beeyard owned by the user."""
    user_id = request.user.id
    beeyard = Beeyards.objects.filter(user__id=user_id)
    hives = Hives.objects.filter(beeyard__in=beeyard)
    interventions = Intervention.objects.filter(hive__in=hives)
    return render(request , 'interventions.html', {'interventions': interventions})


