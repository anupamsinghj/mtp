from django.db import models

# Create your models here.
class COORD(models.Model):

    lat = models.FloatField()
    img = models.ImageField(upload_to='pics')
    lon = models.FloatField()
