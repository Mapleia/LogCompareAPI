# Create your views here.

from rest_framework import viewsets, permissions
from .serializers import EncounterSerializer, FightSerializer
from .models import Encounter, Fight
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

class EncounterViewSets(viewsets.ModelViewSet) :
    queryset = Encounter.objects.all()
    serializer_class = EncounterSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tryID', 'name']


class FightViewSets(viewsets.ModelViewSet) :
    queryset = Fight.objects.all()
    serializer_class = FightSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tryID', 'account']


def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('api')

    else:
        f = UserCreationForm()

    return render(request, 'signup.html', {'form': f})