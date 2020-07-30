from django.db import models
from datetime import time


# Create your models here.

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)


class Room(models.Model):
    name = models.CharField(max_length=200)
    floor = models.IntegerField()
    room_number = models.IntegerField()
