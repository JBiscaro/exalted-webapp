from django.db import models


# Create your models here.
class Charm(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    mote_cost = models.SmallIntegerField(blank=True)
    willpower_cost = models.SmallIntegerField(blank=True)
    anima_cost = models.SmallIntegerField(blank=True)
    bashing_cost = models.SmallIntegerField(blank=True)
    lethal_cost = models.SmallIntegerField(blank=True)
