# serializers.py

from rest_framework import serializers

from .models import Encounter, Boss, Fight

class BossSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boss
        fields = ['name', 'icon']

class FightSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    icon = serializers.SerializerMethodField(read_only=True)

    def get_name(self, obj):
        return obj.boss.name
    
    def get_icon(self, obj):
        return obj.boss.icon

    class Meta:
        model = Fight
        fields = ['tryID', 'name', 'icon', 'permaLink', 'cm']

class EncounterSerializer(serializers.ModelSerializer):
    tryID = serializers.SerializerMethodField(read_only=True)

    def get_tryID(self, obj):
        return obj.fight.tryID
    class Meta:
        model = Encounter
        fields = ['name', 'account', 'archetype', 'DPS', 'tryID']

class PercentileSerializer(serializers.ModelSerializer):
    percentrankdps = serializers.SerializerMethodField(read_only=True)
    percentrankmight = serializers.SerializerMethodField(read_only=True)
    percentrankquickness = serializers.SerializerMethodField(read_only=True)
    percentrankalacrity = serializers.SerializerMethodField(read_only=True)
    percentrankfury = serializers.SerializerMethodField(read_only=True)
    tryID = serializers.SerializerMethodField(read_only=True)

    def get_percentrankdps(self, obj):
        return obj.percentrankdps

    def get_percentrankmight(self, obj):
        return obj.percentrankmight

    def get_percentrankquickness(self, obj):
        return obj.percentrankquickness

    def get_percentrankalacrity(self, obj):
        return obj.percentrankalacrity

    def get_percentrankfury(self, obj):
        return obj.percentrankfury
    
    def get_tryID(self, obj):
        return obj.fight.tryID

    class Meta:
        model = Encounter
        fields = ('tryID', 'account', 'archetype',
                  'percentrankdps', 'percentrankmight', 'percentrankquickness', 'percentrankalacrity',
                  'percentrankfury')
