from datetime import date
from django.db import models
from django.db.models import CASCADE

class Hives(models.Model):
  STATUS_CHOICE = [
    ("En activité", "A"),
    ("En attente", "W"),
    ("Détruite","X"),
  ]
  BEE_TYPE_CHOICE = [("Abeille Italienne" ,"Apis Mellifera Ligustica"),
                    ("Abeille Caucasienne" ,"Apis mellifera caucasica"),
                    ("Abeille Carnolienne" ,"Apis mellifera carnica"),
                    ("Abeille Buckfast", "Abeille hybride"),
                    ("Abeille Charpentière", "Xylocope")]
  name= models.CharField(max_length = 50)
  status= models.CharField(max_length = 50, choices = STATUS_CHOICE)
  beeyard= models.ForeignKey('Beeyards', on_delete = CASCADE,related_name ="hives" )
  last_status_change= models.DateField(auto_now_add = True)
  queen_age= models.BigIntegerField()
  bee_type = models.CharField(choices = BEE_TYPE_CHOICE, max_length = 150)
  
  def __str__(self):
    bee_type_label = dict(self.BEE_TYPE_CHOICE).get(self.bee_type, '')
    status_label = dict(self.STATUS_CHOICE).get(self.status, '')
    return f"{self.id} - {self.name} - {self.status} - {self.last_status_change} - {self.queen_age} - {bee_type_label} - {status_label}"