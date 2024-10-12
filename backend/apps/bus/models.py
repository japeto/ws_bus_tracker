from django.db import models

class Bus(models.Model):
  plate = models.CharField(max_length=100)
  status = models.CharField(max_length=100)
  current_latitudine = models.DecimalField(max_digits=9, decimal_places=6, default=0)
  current_longitudine = models.DecimalField(max_digits=9, decimal_places=6, default=0)  
  
  def __str__(self) -> str:
    return f"Bus [{self.plate}] - status: {self.status}"

# TAREA 1: Crear el modelo Ubicacion Location(latitude, longitude, update_at)  
class Location(models.Model):
  bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='bus_location', unique=False)
  latitude = models.DecimalField(max_digits=9, decimal_places=6)
  longitude = models.DecimalField(max_digits=9, decimal_places=6)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self) -> str:
    return f"Location {self.bus.plate}: ({self.latitude}, {self.longitude})"