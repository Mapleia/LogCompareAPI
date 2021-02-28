# Create your views here.
import requests
from django.db.models import Window, F
from django.db.models.functions import PercentRank
from rest_framework import viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .serializers import EncounterSerializer, PercentileSerializer
from .models import Encounter


def get_archetype(player):
    if player['healing'] > 0:
        return 'HEALER'
    elif player['concentration'] > 0:
        return 'SUPPORT'
    else:
        return 'DPS'


# def get_tryid(data):
#     try_id = 0
#     for player in data['players']:
#         try_id += hash(player['account']) + player['instanceID']

#     return try_id


def parse_json(data, tryid):
    arr = []
    buff_arr = {725: 'fury', 740: 'might', 1187: 'quickness', 30328: 'alacrity'}
    # 725 Fury, 740 Might, 1187 Quickness, 30328 Alacrity

    for player in data['players']:
        p = {
            'name': data['fightName'],
            'gw2Build': data['gW2Build'],
            'tryID': str(tryid),
            'account': player['account'],
            'DPS': player['dpsTargets'][0][0]['dps'],
            'archetype': get_archetype(player)
        }

        for buff in player['buffUptimesActive']:
            if buff['id'] in buff_arr:
                p[buff_arr[buff['id']]] = buff['buffData'][0]['uptime']

        arr.append(Encounter(**p))

    return arr


class EncounterViewSets(viewsets.ModelViewSet):
    queryset = Encounter.objects.all()
    serializer_class = EncounterSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tryID', 'name']

    @action(detail=False, methods=['post'])
    def upload_report(self, req):
        tryid = self.request.query_params.get('id')
        r2 = requests.get('https://dps.report/getJson?id=' + tryid)
        dr_json = r2.json()

        exist = Encounter.objects.filter(tryID=tryid).exists()
        if not exist:
            parsed = parse_json(dr_json, tryid)
            #print(parsed)
            Encounter.objects.bulk_create(parsed)

        return Response({'tryID': tryid,
                         'fightName': dr_json['fightName'],
                         'fightIcon': dr_json['fightIcon']},
                        status=status.HTTP_201_CREATED)


class PercentileViewSets(viewsets.ReadOnlyModelViewSet):
    model = Encounter
    serializer_class = PercentileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    def get_queryset(self):
        def make_boon_rank(boon):
            return Window(expression=PercentRank(), order_by=F(boon).asc())

        dps_rank = Window(expression=PercentRank(), partition_by=[F('archetype'), F('name')], order_by=F('DPS').asc())

        queryset = Encounter.objects.all().annotate(percent_rank=dps_rank, percentrankdps=F('percent_rank')
                                                    ).annotate(percent_rank=make_boon_rank('might'),
                                                               percentrankmight=F('percent_rank')
                                                               ).annotate(
            percent_rank=make_boon_rank('quickness'), percentrankquickness=F('percent_rank')
        ).annotate(percent_rank=make_boon_rank('alacrity'), percentrankalacrity=F('percent_rank')
                   ).annotate(percent_rank=make_boon_rank('fury'), percentrankfury=F('percent_rank'))

        return queryset

    # def list(self, request):
    #     tryid = request.GET.get('tryid', None)
    #     print(tryid)
    #     queryset = self.get_queryset()
    #     if tryid is not None:
    #         # print(list(filter(lambda e: (e.tryID == tryid), list(queryset))))
    #         # print(list(queryset))
    #         for encounter in list(queryset):
    #             if encounter.tryID == tryid:
    #                 print(encounter.tryID)
    #
    #         encounters = [Encounter for encounter in list(queryset) if encounter.tryID == tryid]
    #         # print(encounters)
    #         data = serializers.serialize('json', encounters)
    #         # print(data)
    #         return HttpResponse(data, content_type="application/json")
    #     else:
    #         data = serializers.serialize('json', list(queryset))
    #         print(data)
    #         return HttpResponse(data, content_type="application/json")
