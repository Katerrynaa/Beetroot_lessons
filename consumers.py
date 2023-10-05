from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Message, ProfileUser
import logging 


logger = logging.getLogger(__name__)

class Chat(AsyncWebsocketConsumer):
    async def connect(self):
        logger.info("Websocket connected")
        await self.accept()

async def save_msg(self, message, sender, receiver):
    try:
        send_user = ProfileUser.objects.get(id=sender)
        receive_user = ProfileUser.objects.get(id=receiver)
        new_msg = Message.objects.create(message=message, send_user=send_user, receive_user=receive_user)
        new_msg.save()
    except Exception as a:
        logger.error(f"Error message: {a}")

async def receive(self, data_text):
    try:
        data_json = json.loads(data_text)
        message = data_json['message']
        sender = data_json['sender']
        receiver = data_json['receiver']
        name_sender = data_json['name_sender']
        self.save_msg(message, sender, receiver)
    except Exception as e:
        logger.error(f"Error message: {e}")

    await self.chat({
        'message': message,
        'sender': sender, 
        'receiver': receiver,
        'name_sender': name_sender
    })

async def chat(self,event):
    try:
        message = event['message']
        sender = event['sender']
        receiver = event['receiver']
        name_sender = event['name_sender']
    except Exception as s:
        logger.error(f"Error message: {s}")

    await self.send(data_text=json.dumps({
        'message': message,
        'sender': sender,
        'receiver': receiver,
        'name_sender': name_sender
    }))
