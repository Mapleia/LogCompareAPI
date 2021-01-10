from django.db import models

# 725 Fury, 740 Might, 1187 Quickness, 30328 Alacrity

# BOONS = [717,718,719,725,726,740,743,873,1122,1187,26980,30328];
# BOON_NAMES = ["Protection","Regeneration","Swiftness","Fury","Vigor",
#               "Might","Aegis","Retaliation","Stability","Quickness","Resistance", "Alacrity"];

# Create your models here. 

class Encounter(models.Model):
    name = models.CharField(max_length=40)
    tryID = models.CharField(max_length=40)
    account = models.CharField(max_length=30)
    DPS = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    archetype = models.CharField(max_length=7)
    gw2Build = models.IntegerField()

    #protection = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    #regeneration = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    #swiftness = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    fury = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    #vigor = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    might = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    #aegis = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    #retaliation = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    #stability = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    quickness = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    #resistance = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    alacrity = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    #rg2 = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    #ag2 = models.DecimalField(max_digits=6, decimal_places=3, default=0)
