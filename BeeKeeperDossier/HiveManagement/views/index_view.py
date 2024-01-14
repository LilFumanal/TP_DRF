from django.http import HttpResponse
from django.shortcuts import render


def index_template(request):
  #This is a failed attempt for a navbar.
  menu = {'menu_items': ['beeyards', 'hives', 'interventions']}
  return render(request, 'index.html', menu)
