from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.

class Encounter(models.Model) :
    name = models.CharField(max_length=40)
    tryID = models.IntegerField()
    gw2Build = models.IntegerField()

class Fight(models.Model) :
    tryID = models.IntegerField()
    account = models.CharField(max_length=30)
    DPS = models.IntegerField()
    archetype = models.CharField(max_length=7)

    Protection = models.DecimalField(max_digits=6, decimal_places=3)
    Regeneration = models.DecimalField(max_digits=6, decimal_places=3)
    Swiftness = models.DecimalField(max_digits=6, decimal_places=3)
    Fury = models.DecimalField(max_digits=6, decimal_places=3)
    Vigor = models.DecimalField(max_digits=6, decimal_places=3)
    Might = models.DecimalField(max_digits=6, decimal_places=3)
    Aegis = models.DecimalField(max_digits=6, decimal_places=3)
    Retaliation = models.DecimalField(max_digits=6, decimal_places=3)
    Stability = models.DecimalField(max_digits=6, decimal_places=3)
    Quickness = models.DecimalField(max_digits=6, decimal_places=3)
    RG2 = models.DecimalField(max_digits=6, decimal_places=3)
    AG2 = models.DecimalField(max_digits=6, decimal_places=3)
    Resistance = models.DecimalField(max_digits=6, decimal_places=3)
    Alacrity = models.DecimalField(max_digits=6, decimal_places=3)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )