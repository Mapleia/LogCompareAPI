# serializers.py
from rest_framework import serializers
from .models import Encounter, Fight

class EncounterSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta: 
        model = Encounter
        fields = ('fightID', 'name', 'gw2Build')

class FightSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Fight
        fields = ('fightID', 'account', 'DPS', 'archetype', 'Protection','Regeneration','Swiftness','Fury','Vigor','Might','Aegis','Retaliation','Stability',
        'Quickness','Regeneration2','Aegis2','Resistance', 'Alacrity')