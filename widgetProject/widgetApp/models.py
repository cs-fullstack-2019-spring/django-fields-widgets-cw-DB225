from django.db import models


# Create your models here.
class Cities(models.Model):
    name = models.CharField(max_length=20)
    cityOrOrigin = models.CharField(max_length=30)
    richOrSuperPower = models.CharField(max_length=20)
    whichSuperPower = models.CharField(max_length=20)
    level = models.CharField(max_length=20)
    examples = models.TextField()
