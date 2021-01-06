#serializers.py

from rest_framework import serializers
from .models import Encounter, Fight

class EncounterSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta: 
        model = Encounter
        fields = ('TryID', 'Name', 'Gw2Build')

class FightSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Fight
        fields = ('TryID', 'Account', 'DPS', 'Archetype', 'Protection','Regeneration','Swiftness','Fury','Vigor','Might','Aegis','Retaliation','Stability',
        'Quickness','Resistance', 'Alacrity')