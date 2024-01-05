from django.db import models
from django.db.models import CASCADE

class Intervention(models.Model):
  motif_choice = [("Supp","Suppression cellules royales"),
                  ("Check","Check de santé"),
                  ("Rec","Récolte"),
                  ("Dist","Distribution de sirop"),
                  ("Pose","Pose des hausses"),
                  ("Dest","Destruction"),
                  ("Multi","Multiplication artificielle de l'essaim"),
                  ("Trai", "Traitement")]
  
  hive = models.ForeignKey("Hives", on_delete = CASCADE, related_name="intervention" )
  motif = models.CharField(choices = motif_choice)
  