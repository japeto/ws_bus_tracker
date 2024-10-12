

from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import include, re_path
from .views import *

urlpatterns = [
    re_path(r'$',  ListCreateBuses.as_view(), name="list-create-buses"),
    re_path(r'^(?P<id>\d+)/$', RetrieveUpdateDeleteBus.as_view(), name="retrieve-update-delete-bus"),
    re_path(r'^(?P<id>\d+)/location/$', UpdateBusLocation.as_view(), name="update-bus-location"),
]

urlpatterns = format_suffix_patterns(urlpatterns)