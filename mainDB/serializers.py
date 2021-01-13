# serializers.py

from rest_framework import serializers

from .models import Encounter


class EncounterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Encounter
        fields = '__all__'


class PercentileSerializer(serializers.ModelSerializer):
    percentrankdps = serializers.SerializerMethodField(read_only=True)
    percentrankmight = serializers.SerializerMethodField(read_only=True)
    percentrankquickness = serializers.SerializerMethodField(read_only=True)
    percentrankalacrity = serializers.SerializerMethodField(read_only=True)
    percentrankfury = serializers.SerializerMethodField(read_only=True)

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

    class Meta:
        model = Encounter
        fields = ('tryID', 'account', 'archetype', 'name',
                  'percentrankdps', 'percentrankmight', 'percentrankquickness', 'percentrankalacrity',
                  'percentrankfury')
