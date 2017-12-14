from django.db import models


# Create your models here.
class Charm(models.Model):
    ABILITY_CHOICES = (
        ('brawl', 'BRAWL'),
        ('athletics', 'ATHLETICS'),
        ('occult', 'OCCULT'),
        ('resistance', 'RESISTANCE'),
        ('evocations', 'EVOCATIONS'),
    )

    CHARM_TYPES = (
        ('Simple', 'SIMPLE'),
        ('Supplemental', 'SUPPLEMENTAL'),
        ('Reflexive', 'REFLEXIVE'),
        ('Permanent', 'PERMANENT'),
    )

    name = models.CharField(max_length=255)
    selection = models.ForeignKey(
        'Selection',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    order = models.PositiveSmallIntegerField(blank=True, default=0)
    ability = models.CharField(
        max_length=20,
        choices=ABILITY_CHOICES,
        default='brawl'
    )
    charm_type = models.CharField(
        max_length=20,
        choices=CHARM_TYPES,
        default='Reflexive'
    )
    keywords = models.CharField(max_length=255, blank=True, default='')
    duration = models.CharField(max_length=50, blank=True, default='')
    description = models.TextField(default='t')
    dice_description = models.TextField(default='t', blank=True)
    short_description = models.TextField(default='s')
    slug = models.SlugField(unique=True)
    mote_cost = models.SmallIntegerField(blank=True, default=0)
    willpower_cost = models.SmallIntegerField(blank=True, default=0)
    initiative_cost = models.SmallIntegerField(blank=True, default=0)
    anima_cost = models.SmallIntegerField(blank=True, default=0)
    bashing_cost = models.SmallIntegerField(blank=True, default=0)
    lethal_cost = models.SmallIntegerField(blank=True, default=0)

    def __str__(self):
        return self.name


class Selection(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
