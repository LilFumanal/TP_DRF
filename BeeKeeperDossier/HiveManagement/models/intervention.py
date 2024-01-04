from django.db import models
from django.db.models import CASCADE

class Intervention:
  motif_choice = ["Suppression cellules royales", "Check de santé", "récolte", "Distribution de sirop", "Pose des hausses", "Destruction", "Multiplication artificielle de l'essaim", "Traitement"]
  
  hive = models.ForeignKey("Hives", on_delete = CASCADE, related_name="intervention" )
  motif = models.CharField(choices = motif_choice)
  