#serializers.py

from rest_framework import serializers
from .models import Encounter, Fight

class EncounterSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta: 
        model = Encounter
        fields = ('tryID', 'name', 'gw2Build')

class FightSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Fight
        fields = ('tryID', 'account', 'DPS', 'archetype', 'protection','regeneration',
        'swiftness','fury','vigor','might','aegis','retaliation','stability',
        'quickness','resistance', 'alacrity')