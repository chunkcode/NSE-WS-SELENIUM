from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({
            'type':'connect_established',
            'message':'You are now connected !'
        }))
    def receive(self, text_data):
        message = "Hello"
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message
            }
        )
    def chat_message(self, event):
        message = event['message']
        
        self.send(text_data=json.dumps({
            'type':'NIFTY-INDEX',
            'message':message
        }))
    def chat_message2(self, event):
        message = event['message']
        
        self.send(text_data=json.dumps({
            'type':'NIFTY-50',
            'message':message
        }))
