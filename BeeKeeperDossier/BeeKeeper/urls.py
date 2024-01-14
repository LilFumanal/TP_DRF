"""
URL configuration for BeeKeeper project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from HiveManagement.views import index_view, beeyard_view, hive_view, intervention_view

router = routers.DefaultRouter()
router.register(r'beeyards', beeyard_view.BeeyardViewSet)
router.register(r'hives', hive_view.HiveViewSet)
router.register(r'interventions', intervention_view.InterventionViewSet),

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('beeyards/', beeyard_view.beeyard_template),
    path('beeyards/<int:beeyard_id>/', hive_view.HiveViewSet.as_view({'post': 'create', 'get': 'get_hives'}), name='hives'),
    path('beeyards/<int:beeyard_id>/interventions/', intervention_view.InterventionViewSet.as_view({'post': 'bulk_creation'}), name='bulk_creation'), #failed_attempt, not working
    path('interventions/', intervention_view.InterventionViewSet.as_view({'post': 'create'}), name='interventions'),
]
