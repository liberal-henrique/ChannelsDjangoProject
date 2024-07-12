import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import AnonymousUser

class ChatConsumer(AsyncWebsocketConsumer):
    rooms = {}

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        if self.room_name not in ChatConsumer.rooms:
            ChatConsumer.rooms[self.room_name] = set()
        ChatConsumer.rooms[self.room_name].add(self.channel_name)

        await self.accept()
    #

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        if self.room_name in ChatConsumer.rooms:
            ChatConsumer.rooms[self.room_name].discard(self.channel_name)
            if not ChatConsumer.rooms[self.room_name]:
                del ChatConsumer.rooms[self.room_name]
    #

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        if self.scope["user"] == AnonymousUser():
            username = 'Anonymous'
        else:
            username = self.scope["user"].username
        print(f'Received message from {username}: {message}')

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'username':username 
            }
        )
    #

    async def chat_message(self, event:str):
        message = event['message']
        username = event['username']
        print(f'Sending message from {username}: {message}')

        await self.send(text_data=json.dumps({
            'message':message,
            'username':username 
        }))
    #