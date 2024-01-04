from datetime import date
from django.db import models

class Hives(models.Model):
  status_choice = [
    ("A", "En activité"),
    ("W", "En attente"),
    ("X", "Détruite"),
  ]
  bee_type_choice= [("Abeille Noire" , "Apis Mellifera Mellifera"),
                    ("Abeille Italienne" ,"Apis Mellifera Ligustica"),
                    ("Abeille Caucasienne" ,"Apis mellifera caucasica"),
                    ("Abeille Carnolienne" ,"Apis mellifera carnica"),
                    ("Abeille Buckfast", "Abeille hybride"),
                    ("Abeille Charpentière", "Xylocope")]
  status= models.CharField(max_length = 50, choices = status_choice)
  last_status_change= models.DateField()
  queen_age= models.BigIntegerField()
  bee_type = models.CharField(choices = bee_type_choice, max_length = 150)
  harvests = { "qté" : int,
              "date" : date ,}
  contamination = { "date": date ,
                  "decease" : str,}
  