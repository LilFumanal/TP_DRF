from django.http import HttpResponse
from django.shortcuts import render


def intervention_template(request):
  return render(request, 'interventions.html')