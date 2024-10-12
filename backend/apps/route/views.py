from rest_framework import generics, status
from rest_framework.response import Response
from .models import Route, Station, RouteStation
from .serializer import RouteSerializer, StationSerializer, RouteStationSerializer

# Route Views
class ListCreateRoutes(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    def create(self, request, *args, **kwargs):
        serializer = RouteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetrieveUpdateDeleteRoute(generics.RetrieveUpdateDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    lookup_field = 'id'


# Station Views
class ListCreateStations(generics.ListCreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

    def create(self, request, *args, **kwargs):
        serializer = StationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetrieveUpdateDeleteStation(generics.RetrieveUpdateDestroyAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    lookup_field = 'id'


# RouteStation Views
class ListCreateRouteStations(generics.ListCreateAPIView):
    queryset = RouteStation.objects.all()
    serializer_class = RouteStationSerializer

    def create(self, request, *args, **kwargs):
        serializer = RouteStationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetrieveUpdateDeleteRouteStation(generics.RetrieveUpdateDestroyAPIView):
    queryset = RouteStation.objects.all()
    serializer_class = RouteStationSerializer
    lookup_field = 'id'
