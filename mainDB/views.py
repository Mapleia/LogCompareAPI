# Create your views here.

from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import EncounterSerializer, FightSerializer
from .models import Encounter, Fight


class EncounterViewSets(viewsets.ModelViewSet) :
    queryset = Encounter.objects.all()
    serializer_class = EncounterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tryID', 'name']


class FightViewSets(viewsets.ModelViewSet) :
    queryset = Fight.objects.all()
    serializer_class = FightSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tryID', 'account']