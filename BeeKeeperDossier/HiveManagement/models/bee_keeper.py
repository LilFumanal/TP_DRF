from django.db import models

class Beekeepers(models.Model):
  email = models.EmailField()
  username: str = models.CharField(max_length = 50)
  name: str = models.CharField(max_length = 50)
  surname: str = models.CharField(max_length = 50)