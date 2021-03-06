# Create your views here.
import requests
from django.db.models import Window, F
from django.db.models.functions import PercentRank
from rest_framework import viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
import json

from .serializers import EncounterSerializer, FightSerializer, PercentileSerializer, BossSerializer
from .models import Encounter, Boss, Fight


def get_archetype(player):
    if player['healing'] > 0:
        return 'HEALER'
    elif player['concentration'] > 0:
        return 'SUPPORT'
    else:
        return 'DPS'

def parse_json(data, fight, boss):
    arr = []
    buff_arr = {725: 'fury', 740: 'might', 1187: 'quickness', 30328: 'alacrity'}
    # 725 Fury, 740 Might, 1187 Quickness, 30328 Alacrity

    for player in data['players']:
        p = {
            'name': boss,
            'fight': fight,
            'account': player['account'],
            'DPS': player['dpsAll'][0]['dps'],
            'archetype': get_archetype(player)
        }

        for buff in player['buffUptimesActive']:
            if buff['id'] in buff_arr:
                p[buff_arr[buff['id']]] = buff['buffData'][0]['uptime']

        arr.append(Encounter(**p))

    return arr

def get_boss_name(uploadJson):
    boss_name = str(uploadJson['encounter']['boss']).strip().removesuffix(" CM")
    return boss_name

class EncounterViewSets(viewsets.ModelViewSet):
    queryset = Encounter.objects.all()
    serializer_class = EncounterSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'account']

    @action(detail=False, methods=['get'])
    def get_encounters(self, request):
        if  request.GET['tryID'] is not None:
            data = list(Encounter.objects.filter(fight__tryID=request.GET['tryID']).values())
            return JsonResponse(data, safe=False)
        else:
            return HttpResponse(status=204)
    @action(detail=False, methods=['get'])
    def account_getID(self, request):
        if  request.GET['account'] is not None:
            data = list(Encounter.objects.filter(account=request.GET['account']).values_list('tryID', flat=True).distinct())
            return JsonResponse(data, safe=False)
        else:
            return HttpResponse(status=204)

class BossViewSets(viewsets.ModelViewSet):
    queryset = Boss.objects.all()
    serializer_class = BossSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    @action(detail=False, methods=['post'])
    def post_missing(self, request):
        body = json.loads(request.body)
        if type(body) is list:
            batch = [Boss(name=obj['name'], icon=obj['icon']) for obj in body]
            Boss.objects.bulk_create(batch)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['delete'])
    def delete_dupes(self, request):
        lastSeenId = float('-Inf')
        rows = Boss.objects.all().order_by('name')

        for row in rows:
            if row.name == lastSeenId:
                row.delete() # We've seen this id in a previous row
            else: # New id found, save it and check future rows for duplicates.
                lastSeenId = row.name 
        return Response(status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        Boss.objects.all().delete()
        return Response(status=status.HTTP_200_OK)

class FightViewSets(viewsets.ModelViewSet):
    queryset = Fight.objects.all()
    serializer_class = FightSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tryID']
    
    @action(detail=False, methods=['get'])
    def account_fight(self, request):
        if request.GET['account'] is not None:
            listed = list(Encounter.objects.filter(account=request.GET['account']).values_list('fight', flat=True).distinct())
            data = Fight.objects.filter(id__in=listed)
            return JsonResponse(FightSerializer(data, many=True, context={'request': request}).data, safe=False)
        else:
            return HttpResponse(status=204)

    @action(detail=False, methods=['post'])
    def upload_report(self, request):        
        input = None
        if request.FILES:
                print(request.FILES)
                input = request.FILES
                metaDataSend = requests.post('https://dps.report/uploadContent?generator=ei&json=1', files=input)
                print('Uploading file.')

        # if link input
        else:
            body = request.data
            if body['link'] is not None:
                input = body['link'].rstrip('/')
                metaDataSend = requests.get('https://dps.report/getUploadMetadata?permalink='+ input)
                print('Finding through permalink.')

        uploadJson = metaDataSend.json()
        # if dps.report getting uploaded meta info is unsuccesful 
        if not metaDataSend.ok:
            return Response({'error': uploadJson['error'], 'input': input}, status=status.HTTP_400_BAD_REQUEST)
        
        boss_name = get_boss_name(uploadJson)
        print(boss_name)
        # if fight exist, find icon link from db, and send the upload metadata
        boss = Boss.objects.get(name=boss_name)
        fight, f_created = Fight.objects.get_or_create(boss=boss, 
            tryID=uploadJson['id'], 
            gw2Build=uploadJson["encounter"]['gw2Build'],
            permaLink=uploadJson['permalink'],
            cm=uploadJson["encounter"]['isCm'])

        drJson = None
        if f_created:
            print("Fight created.")
            send = requests.get('https://dps.report/getJson?id=' + uploadJson['id'])
            drJson = send.json()
            if send.ok:
                parsed = parse_json(drJson, fight, boss_name)
                Encounter.objects.bulk_create(parsed)
                return JsonResponse(FightSerializer(fight, context={'request': request}).data, safe=False, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': drJson, 'input': input}, status=status.HTTP_400_BAD_REQUEST)
        else:            
            return JsonResponse(FightSerializer(fight, context={'request': request}).data, safe=False, status=status.HTTP_200_OK)


class PercentileViewSets(viewsets.ReadOnlyModelViewSet):
    model = Encounter
    serializer_class = PercentileSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        def make_boon_rank(boon):
            return Window(expression=PercentRank(), partition_by=[F('name')], order_by=F(boon).asc())

        dps_rank = Window(expression=PercentRank(), partition_by=[F('archetype'), F('name')], order_by=F('DPS').asc())

        queryset = Encounter.objects.annotate(percent_rank=dps_rank, percentrankdps=F('percent_rank')
                                                    ).annotate(percent_rank=make_boon_rank('might'),
                                                               percentrankmight=F('percent_rank')
                                                               ).annotate(
            percent_rank=make_boon_rank('quickness'), percentrankquickness=F('percent_rank')
        ).annotate(percent_rank=make_boon_rank('alacrity'), percentrankalacrity=F('percent_rank')
                   ).annotate(percent_rank=make_boon_rank('fury'), percentrankfury=F('percent_rank'))

        return queryset
