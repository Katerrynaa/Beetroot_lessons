from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Message, ProfileUser
import logging 

logger = logging.getLogger(__name__)

class Chat(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({'message': "Websocket connected"}))

    async def disconnect(self):
        self.send(text_data=json.dumps({'message': 'Websocket disconnected'}))

    async def receive(self, text_data):
        data_json = json.loads(text_data)
        message = data_json['message']
        sender = data_json['sender']
        receiver = data_json['receiver']
        name_sender = data_json['name_sender']

        await self.save_msg(message, sender, receiver)

        await self.send(text_data=json.dumps(
            {
                'message': message,
                'sender': sender,
                'receiver': receiver,
                'name_sender': name_sender
            }
        ))

    async def save_msg(self, message, sender, receiver):
        try:
            send_user = ProfileUser.objects.get(id=sender)
            receive_user = ProfileUser.objects.get(id=receiver)
            new_msg = Message.objects.create(message=message, send_user=send_user, receive_user=receive_user)
            new_msg.save()
        except Exception as a:
            logger.error(f"Error message: {a}")
