from django.contrib.gis.db import models


class Type(models.Model):
    name = models.CharField(max_length=64, blank=False)
    description = models.CharField(max_length=64, blank=False)

    def __str__(self):
        return self.name
