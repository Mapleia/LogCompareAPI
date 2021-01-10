# Create your views here.
from django.db.models import Window, F
from django.db.models.functions import PercentRank
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import EncounterSerializer, FightSerializer, PercentileSerializer
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
    serializer_class = PercentileSerializer

    def get_queryset(self):
        dps_rank = Window(expression=PercentRank(), partition_by=F('archetype'), order_by=F('DPS').asc())
        
        def make_boon_rank(boon) :
            return Window(
                expression=PercentRank(),
                order_by=F(boon).desc())

        query_name = self.request.query_params.get('name', None)
        query_id = self.request.query_params.get('tryid', None)
        print(query_name)
        print(query_id)
        if query_name and query_id is not None:
            encounters = list(Encounter.objects.filter(name=query_name).values_list('tryID', flat=True))
            print('Encounter:')
            print(encounters)

            fights_filtered = Fight.objects.filter(tryID__in=encounters)
            dps = fights_filtered.annotate(percent_rank=dps_rank,  rank_dps=F('percent_rank')).order_by('archetype').values('tryID', 'account', 'DPS', 'archetype', 'percent_rank')
            might = fights_filtered.annotate(percent_rank=make_boon_rank('might')).values('tryID', 'account', 'DPS','archetype', 'percent_rank')    
            quick = fights_filtered.annotate(percent_rank=make_boon_rank('quickness')).values('tryID', 'account', 'DPS','archetype', 'percent_rank') 
            alac = fights_filtered.annotate(percent_rank=make_boon_rank('alacrity')).values('tryID', 'account', 'DPS','archetype', 'percent_rank') 
            fury = fights_filtered.annotate(percent_rank=make_boon_rank('fury')).values('tryID', 'account', 'DPS','archetype', 'percent_rank') 

            print(dps.query)
            #print(might.query)
            #print(quick.query)
            #print(alac.query)
            return dps