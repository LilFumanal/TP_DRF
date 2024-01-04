from django.db import models

class Beeyards(models.Model):
  nom : str = models.CharField(max_length = 50)
  user = models.ForeignKey('Beekeepers', on_delete = models.CASCADE, related_name="beeyard")