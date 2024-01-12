from django.db import models
from django.db.models import CASCADE

class Intervention(models.Model):
  MOTIF_CHOICES = [("Supp","Suppression cellules royales"),
                  ("Check","Check de santé"),
                  ("Rec","Récolte"),
                  ("Dist","Distribution de sirop"),
                  ("Pose","Pose des hausses"),
                  ("Dest","Destruction"),
                  ("Multi","Multiplication artificielle de l'essaim"),
                  ("Trai", "Traitement")]
  
  hive = models.ForeignKey("Hives", on_delete = CASCADE, related_name="intervention" )
  motif = models.CharField(choices = MOTIF_CHOICES)
  date = models.DateField()
  harvest_quantity = models.IntegerField(blank=True)
  is_sick = models.BooleanField()
  decease = models.CharField(max_length = 50, blank=True)
  
  def __str__(self):
    motif_label = dict(self.MOTIF_CHOICES).get(self.motif, '')
    return f"{self.hive} - {self.date} - {motif_label}"