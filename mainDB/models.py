from django.db import models
# BOONS = [717,718,719,725,726,740,743,873,1122,1187,26980,30328];
# BOON_NAMES = ["Protection","Regeneration","Swiftness","Fury","Vigor",
#               "Might","Aegis","Retaliation","Stability","Quickness","Resistance", "Alacrity"];

# Create your models here.
class Encounter(models.Model) :
    Name = models.CharField(max_length=40)
    TryID = models.BigIntegerField()
    Gw2Build = models.IntegerField()

class Fight(models.Model) :
    tryID = models.IntegerField()
    Account = models.CharField(max_length=30)
    DPS = models.IntegerField()
    Archetype = models.CharField(max_length=7)

    Protection = models.DecimalField(max_digits=6, decimal_places=3, default=0, editable=False)
    Regeneration = models.DecimalField(max_digits=6, decimal_places=3, default=0, editable=False)
    Swiftness = models.DecimalField(max_digits=6, decimal_places=3, default=0, editable=False)
    Fury = models.DecimalField(max_digits=6, decimal_places=3, default=0, editable=False)
    Vigor = models.DecimalField(max_digits=6, decimal_places=3, default=0, editable=False)
    Might = models.DecimalField(max_digits=6, decimal_places=3, default=0, editable=False)
    Aegis = models.DecimalField(max_digits=6, decimal_places=3, default=0, editable=False)
    Retaliation = models.DecimalField(max_digits=6, decimal_places=3, default=0, editable=False)
    Stability = models.DecimalField(max_digits=6, decimal_places=3, default=0, editable=False)
    Quickness = models.DecimalField(max_digits=6, decimal_places=3, default=0, editable=False)
    Resistance = models.DecimalField(max_digits=6, decimal_places=3, default=0, editable=False)
    Alacrity = models.DecimalField(max_digits=6, decimal_places=3, default=0, editable=False)
