import json
from channels.generic.websocket import AsyncWebsocketConsumer

class GameConsumer(AsyncWebsocketConsumer):
    rooms = {}

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'game_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        if self.room_group_name not in GameConsumer.rooms:
            GameConsumer.rooms[self.room_name] = set()
        GameConsumer.rooms[self.room_name].add(self.channel_name)

        await self.accept()
        print(f"WebSocket connected: {self.room_name}")
    #

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)

        print(f"Received full data: {data}")

        message_type = data.get('type')
        paddle_position = None
        ball_position = None

        if message_type == 'client_update':
            paddle_position = data.get('paddle_position')
            print(f"Received client paddle position: {paddle_position}")
        elif message_type == 'host_update':
            paddle_position = data.get('paddle_position')
            ball_position = data.get('ball')
            print(f"Received client paddle position: {paddle_position}")
            print(f"Received ball position: {ball_position}")

        # host_update = data.get('host_Update')
        # client_update = data.get('client_update')

        # print(f"Received client position: {client_update}")
        # print(f"Received host position: {host_update}")


        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'game_update',
                'paddle_position': paddle_position,
            }
        )
    #

    async def game_update(self, event):
        paddle_position = event['paddle_position']

        await self.send(text_data=json.dumps({
            'paddle_position': paddle_position
        }))
#
