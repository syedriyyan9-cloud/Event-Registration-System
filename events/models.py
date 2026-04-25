from django.db import models
from django.conf import settings

# Create your models here.
class Events(models.Model):
    '''columns for event'''
    event_name = models.CharField(max_length=200)
    event_venue = models.CharField(max_length=200 )
    event_date = models.DateTimeField()
    event_capacity = models.IntegerField()
    event_type = models.CharField(max_length=200 )
    event_details = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events')