from django.contrib.gis.db import models
from .TypeModel import Type


class Object(models.Model):
    name = models.CharField(max_length=64, blank=False)
    description = models.CharField(max_length=64, blank=False)
    geom = models.PointField(srid=4326)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
