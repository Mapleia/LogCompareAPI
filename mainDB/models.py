from django.db import models


# 725 Fury, 740 Might, 1187 Quickness, 30328 Alacrity

# BOONS = [717,718,719,725,726,740,743,873,1122,1187,26980,30328];
# BOON_NAMES = ["Protection","Regeneration","Swiftness","Fury","Vigor",
#               "Might","Aegis","Retaliation","Stability","Quickness","Resistance", "Alacrity"];

# Create your models here. 

class Boss(models.Model):
    name = models.CharField(max_length=40)
    icon = models.URLField()

class Fight(models.Model):
    boss = models.ForeignKey(Boss, on_delete=models.CASCADE)
    tryID = models.CharField(max_length=40)
    gw2Build = models.IntegerField()
    permaLink = models.URLField()
    cm = models.BooleanField(default=False)


class Encounter(models.Model):
    name = models.CharField(max_length=30)
    fight = models.ForeignKey(Fight, on_delete=models.CASCADE)
    account = models.CharField(max_length=30)
    archetype = models.CharField(max_length=7)
    DPS = models.IntegerField()
    fury = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    might = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    quickness = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    alacrity = models.DecimalField(max_digits=6, decimal_places=3, default=0)