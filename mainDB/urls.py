from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'encounters', views.EncounterViewSets, basename='encounters')
#router.register(r'fights', views.FightViewSets, basename='fights')
router.register(r'percentiles', views.PercentileViewSets, basename='percentiles')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
