import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Bus, Location

class BusLocationConsumer(AsyncWebsocketConsumer):
    """Bus location consumer

    Args:
        AsyncWebsocketConsumer (_type_): _description_
    """
    async def connect(self):
        self.bus_id = self.scope['url_route']['kwargs']['bus_id']
        self.bus_group_name = f'bus_{self.bus_id}'
        
        print(f"### -  {self.bus_id}, {self.bus_group_name}")
        
        await self.channel_layer.group_add(
            self.bus_group_name,
            self.channel_name
        )
        await self.accept()
        
    async def disconnect(self, close_code):
        # Leave the bus group
        await self.channel_layer.group_discard(
            self.bus_group_name,
            self.channel_name
        )

    # Receive message from WebSocket (client sends data to update the location)
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        latitude = text_data_json['latitude']
        longitude = text_data_json['longitude']

        # Update the location in the database
        bus = Bus.objects.get(id=self.bus_id)
        location, created = Location.objects.get_or_create(bus=bus)
        location.latitude = latitude
        location.longitude = longitude
        location.save()

        # Broadcast the updated location to the group (to other clients)
        await self.channel_layer.group_send(
            self.bus_group_name,
            {
                'type': 'bus_location_update',
                'latitude': latitude,
                'longitude': longitude
            }
        )

    # Receive a location update from the group (broadcast to all clients)
    async def bus_location_update(self, event):
        print("### bus_location_update")
        # location = event['location']
        latitude = event['latitude']
        longitude = event['longitude']

        # Send the updated location to the WebSocket (client)
        await self.send(text_data=json.dumps({
            'latitude': latitude,
            'longitude': longitude
        }))
