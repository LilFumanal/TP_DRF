from django.db import models
from django.contrib.auth.models import User

class Beeyards(models.Model):
  name = models.CharField(max_length = 50)
  user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="beeyard")
  
  def __str__(self):
    return f"{self.name} - {self.user}"