from django.db import models

class Route(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Station(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

class RouteStation(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='route_stations')
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='station_routes')
    order = models.PositiveIntegerField()

    class Meta:
        unique_together = ('route', 'station', 'order')  # To ensure a station appears only once per route at a specific order
        ordering = ['order']  # Stations are ordered by their order number along the route

    def __str__(self):
        return f"{self.station.name} on {self.route.name} (Order: {self.order})"
