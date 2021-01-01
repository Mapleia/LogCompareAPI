from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'encounters', views.EncounterViewSets)
router.register(r'fights', views.FightViewSets)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls), name="api"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]