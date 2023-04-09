from django.db import models
from datetime import time

# Create your models here.
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)    ### in hours
    
    def __str__(self) -> str:
        return f"{self.title} at {self.start_time} on {self.date}"