import json

from channels.generic.websocket import AsyncWebsocketConsumer

class GameConsumer(AsyncWebsocketConsumer):
    rooms = {}
    
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'game_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_name,
            self.room_group_name
        )

        if self.room_name not in self.rooms:
            self.rooms[self.room_name] = {
                'players': [],
                'state': {}
            }
        #
        self.rooms[self.room_name]['players'].append(self.channel_name)

        await self.accept()
    #
#
