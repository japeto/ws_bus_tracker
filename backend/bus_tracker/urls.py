from django.contrib import admin
from django.urls import include, re_path

urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path(r'^api/buses/', include('apps.bus.urls')),
    re_path(r'^api/', include('apps.route.urls'))
]