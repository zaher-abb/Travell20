from django.db import models
from datetime import datetime,date


class Destination(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    des = models.TextField()
    price = models.IntegerField(default=0)
    offer = models.BooleanField(default=False)
    start=models.DateField(blank=True,null=True)
    end = models.DateField(blank=True, null=True)

    def __str__(self):

        return self.name


