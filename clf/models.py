from time import time
from django.db import models

# Create your models here.
class entries(models.Model):

    v1 = models.IntegerField(default=0)
    v2 = models.IntegerField(default=0)
    v3 = models.IntegerField(default=0)
    v4 = models.IntegerField(default=0)
    the_kind = models.CharField(max_length=100)
    prediction_time = models.CharField(max_length=100)