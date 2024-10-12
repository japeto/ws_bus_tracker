from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import re_path
from .views import *

urlpatterns = [
    # Routes
    re_path(r'^routes/$', ListCreateRoutes.as_view(), name="list-create-routes"),
    re_path(r'^routes/(?P<id>\d+)/$', RetrieveUpdateDeleteRoute.as_view(), name="retrieve-update-delete-route"),

    # Stations
    re_path(r'^stations/$', ListCreateStations.as_view(), name="list-create-stations"),
    re_path(r'^stations/(?P<id>\d+)/$', RetrieveUpdateDeleteStation.as_view(), name="retrieve-update-delete-station"),

    # RouteStations (Route to Station mapping with order)
    re_path(r'^routestations/$', ListCreateRouteStations.as_view(), name="list-create-route-stations"),
    re_path(r'^routestations/(?P<id>\d+)/$', RetrieveUpdateDeleteRouteStation.as_view(), name="retrieve-update-delete-route-station"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
