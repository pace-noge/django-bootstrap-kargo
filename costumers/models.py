from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    driver = models.CharField(max_length=200)
    number = models.IntegerField()
    capacity = models.IntegerField()
    photo = models.FileField(upload_to='')

    def __unicode__(self):
        return self.name