#serializers.py

from rest_framework import serializers
from .models import Encounters, Fights

class EncounterSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta: 
        model = Encounters
        fields = ('tryID', 'name', 'gw2Build')

class FightSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Fights
        fields = ('tryID', 'account', 'DPS', 'archetype', 'protection','regeneration',
        'swiftness','fury','vigor','might','aegis','retaliation','stability',
        'quickness','resistance', 'alacrity')