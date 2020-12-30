from django.db import models

# Create your models here.

class Encounter(models.Model) :
    name = models.CharField(max_length=40)
    fightID = models.IntegerField()
    gw2Build = models.IntegerField()

class Fight(models.Model) :
    fightID = models.IntegerField()
    account = models.CharField(max_length=30)
    DPS = models.IntegerField()
    archetype = models.CharField(max_length=7)

    Protection = models.DecimalField(max_digits=6, decimal_places=3)
    Regeneration = models.DecimalField(max_digits=6, decimal_places=3)
    Swiftness = models.DecimalField(max_digits=6, decimal_places=3)
    Fury = models.DecimalField(max_digits=6, decimal_places=3)
    Vigor = models.DecimalField(max_digits=6, decimal_places=3)
    Might = models.DecimalField(max_digits=6, decimal_places=3)
    Aegis = models.DecimalField(max_digits=6, decimal_places=3)
    Retaliation = models.DecimalField(max_digits=6, decimal_places=3)
    Stability = models.DecimalField(max_digits=6, decimal_places=3)
    Quickness = models.DecimalField(max_digits=6, decimal_places=3)
    Regeneration2 = models.DecimalField(max_digits=6, decimal_places=3)
    Aegis2 = models.DecimalField(max_digits=6, decimal_places=3)
    Resistance = models.DecimalField(max_digits=6, decimal_places=3)
    Alacrity = models.DecimalField(max_digits=6, decimal_places=3)