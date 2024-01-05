from django.http import HttpResponse
from django.shortcuts import render


def index_template(request):
  menu = {'menu_items': ['Mon accueil', 'Cheptels', 'Ruches', 'Interventions']}
  return render(request, 'index.html')
