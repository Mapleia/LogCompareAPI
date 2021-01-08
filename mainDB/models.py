from django.db import models
# BOONS = [717,718,719,725,726,740,743,873,1122,1187,26980,30328];
# BOON_NAMES = ["Protection","Regeneration","Swiftness","Fury","Vigor",
#               "Might","Aegis","Retaliation","Stability","Quickness","Resistance", "Alacrity"];

# Create your models here.
class Encounters(models.Model) :
    name = models.CharField(max_length=40)
    tryID = models.BigIntegerField()
    gw2Build = models.IntegerField()

class Fights(models.Model) :
    tryID = models.IntegerField()
    account = models.CharField(max_length=30)
    DPS = models.IntegerField()
    archetype = models.CharField(max_length=7)

    protection = models.DecimalField(max_digits=6, decimal_places=3, default=0, editable=False)
    regeneration = models.DecimalField(max_digits=6, decimal_places=3, default=0, editable=False)
    swiftness = models.DecimalField(max_digits=6, decimal_places=3, default=0, editable=False)
    fury = models.DecimalField(max_digits=6, decimal_places=3, default=0, editable=False)
    vigor = models.DecimalField(max_digits=6, decimal_places=3, default=0, editable=False)
    might = models.DecimalField(max_digits=6, decimal_places=3, default=0, editable=False)
    aegis = models.DecimalField(max_digits=6, decimal_places=3, default=0, editable=False)
    retaliation = models.DecimalField(max_digits=6, decimal_places=3, default=0, editable=False)
    stability = models.DecimalField(max_digits=6, decimal_places=3, default=0, editable=False)
    quickness = models.DecimalField(max_digits=6, decimal_places=3, default=0, editable=False)
    resistance = models.DecimalField(max_digits=6, decimal_places=3, default=0, editable=False)
    alacrity = models.DecimalField(max_digits=6, decimal_places=3, default=0, editable=False)
