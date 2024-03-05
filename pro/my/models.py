from django.db import models

class Event(models.Model):
    date = models.IntegerField()
    month = models.IntegerField()
    name = models.CharField(max_length=100)


# Create your models here.
