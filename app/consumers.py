from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
class MyCon(SyncConsumer):

    def websocket_connect (self,event):
        async_to_sync(self.channel_layer.group_add('nifty', self.channel_name))
        self.send({
            'type':'websocket.accept'
        })
    def websocket_receive (self,event):
        #  self.send({
        #     'type':'websocket.send',
        #     'text':'hi'
        # })
         channel_layer = get_channel_layer()
         async_to_sync(channel_layer.group_send('nifty',  {'type':'Hello'}))
    def websocket_disconnect (self,event):
        print("someone disconnected",event)
        raise StopConsumer()