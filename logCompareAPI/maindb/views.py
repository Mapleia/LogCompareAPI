
# Create your views here.

from rest_framework import viewsets, permissions
from .serializers import EncounterSerializer, FightSerializer
from .models import Encounter, Fight
from django_filters.rest_framework import DjangoFilterBackend

class EncounterViewSets(viewsets.ModelViewSet) :
    queryset = Encounter.objects.all()
    serializer_class = EncounterSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['fightID', 'name']


class FightViewSets(viewsets.ModelViewSet) :
    queryset = Fight.objects.all()
    serializer_class = FightSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['fightID', 'account']
