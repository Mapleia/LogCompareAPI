# Create your views here.
from django.db.models import Window, F
from django.db.models.functions import PercentRank
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import EncounterSerializer, FightSerializer
from .models import Encounter, Fight


class EncounterViewSets(viewsets.ModelViewSet):
    queryset = Encounter.objects.all()
    serializer_class = EncounterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tryID', 'name']


class FightViewSets(viewsets.ModelViewSet):
    queryset = Fight.objects.all()
    serializer_class = FightSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tryID', 'account']


class PercentileViewSets(viewsets.ReadOnlyModelViewSet):
    serializer_class = FightSerializer

    def get_queryset(self):
        query_name = self.request.query_params.get('name', None)
        if query_name is not None:
            encounters = Encounter.objects.filter(name=query_name).values_list('tryID')
            fights = Fight.objects.filter(tryID__in=encounters).annotate(percent_rank=Window(
                expression=PercentRank(),
                partition_by=F('archetype'),
                order_by=F('tryID').asc()
            ))
            return fights
