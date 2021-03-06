from django.contrib import admin
from .models import Encounter, Boss, Fight
# Register your models here.

admin.site.register(Encounter)
admin.site.register(Boss)
admin.site.register(Fight)

