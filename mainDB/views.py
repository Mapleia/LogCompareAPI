# Create your views here.
from django.db.models import Window, F
from django.db.models.functions import PercentRank
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import EncounterSerializer, PercentileSerializer
from .models import Encounter


class EncounterViewSets(viewsets.ModelViewSet):
    queryset = Encounter.objects.all()
    serializer_class = EncounterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tryID', 'name']


class PercentileViewSets(viewsets.ReadOnlyModelViewSet):
    serializer_class = PercentileSerializer

    def get_queryset(self):
        def make_boon_rank(boon):
            return Window(
                expression=PercentRank(),
                order_by=F(boon).asc())

        query_name = self.request.query_params.get('name', None)

        if query_name is not None:
            dps_rank = Window(expression=PercentRank(), partition_by=F('archetype'), order_by=F('DPS').asc())

            encounters = Encounter.objects.filter(name=query_name
                                                  ).annotate(percent_rank=dps_rank, percentrankdps=F('percent_rank')
                                                             ).annotate(percent_rank=make_boon_rank('might'),
                                                                        percentrankmight=F('percent_rank')
                                                                        ).annotate(
                percent_rank=make_boon_rank('quickness'), percentrankquickness=F('percent_rank')
                ).annotate(percent_rank=make_boon_rank('alacrity'), percentrankalacrity=F('percent_rank')
                           ).annotate(percent_rank=make_boon_rank('fury'), percentrankfury=F('percent_rank')
                                      ).order_by('DPS')

            return encounters

            """ 
            SELECT `mainDB_encounter`.`account`, `mainDB_encounter`.`DPS`, `mainDB_encounter`.`archetype`, 
            PERCENT_RANK() OVER (PARTITION BY `mainDB_encounter`.`archetype` ORDER BY `mainDB_encounter`.`DPS` ASC) AS `percentrankdps`,
            PERCENT_RANK() OVER (ORDER BY `mainDB_encounter`.`might` ASC) AS `percentrankmight`,
            PERCENT_RANK() OVER (ORDER BY `mainDB_encounter`.`quickness` ASC) AS `percentrankquickness`,
            PERCENT_RANK() OVER (ORDER BY `mainDB_encounter`.`alacrity` ASC) AS `percentrankalacrity`,
            PERCENT_RANK() OVER (ORDER BY `mainDB_encounter`.`fury` ASC) AS `percentrankfury` 
            FROM `mainDB_encounter` WHERE `mainDB_encounter`.`name` = 'Nightmare Oratuss'
            ORDER BY `mainDB_encounter`.`fury` ASC;
            """
