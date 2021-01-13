# Create your views here.
from django.db.models import Window, F
from django.db.models.functions import PercentRank
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import EncounterSerializer, PercentileSerializer
from .models import Encounter


class EncounterViewSets(viewsets.ModelViewSet):
    queryset = Encounter.objects.all()
    serializer_class = EncounterSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tryID', 'name']

    #@action(detail=False, methods=['post'])
    #def upload_dpsreport(self, request):



class PercentileViewSets(viewsets.ReadOnlyModelViewSet):
    model = Encounter
    serializer_class = PercentileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    def get_queryset(self):
        def make_boon_rank(boon):
            return Window(expression=PercentRank(), order_by=F(boon).asc())

        dps_rank = Window(expression=PercentRank(), partition_by=F('archetype'), order_by=F('DPS').asc())

        queryset = Encounter.objects.annotate(percent_rank=dps_rank, percentrankdps=F('percent_rank')
                                            ).annotate(percent_rank=make_boon_rank('might'),
                                                       percentrankmight=F('percent_rank')
                                            ).annotate( percent_rank=make_boon_rank('quickness'),
                                                        percentrankquickness=F('percent_rank')
                                            ).annotate(percent_rank=make_boon_rank('alacrity'),
                                                       percentrankalacrity=F('percent_rank')
                                            ).annotate(percent_rank=make_boon_rank('fury'),
                                                       percentrankfury=F('percent_rank')
                                                       ).order_by('DPS')
        return queryset