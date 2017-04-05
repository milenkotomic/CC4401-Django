from __future__ import unicode_literals

from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.IntegerField(default=0)
    license_plate = models.CharField(max_length=10)
    
    def __str__(self):
        return self.license_plate
    
    
class Reservation(models.Model):
    start = models.DateField()
    end = models.DateField()
    car =  models.ForeignKey(Car, on_delete=models.CASCADE)
    

