import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class WalletConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'client_wallet'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name)
        self.accept()
        
    # def disconnect(self, close_code):
    #     async_to_sync(self.channel_layer.group_discard)(
    #         self.room_group_name, self.channel_name)
        
    def receive(self, text_data):
        data = json.loads(text_data)
        message = data['client_data']
        async_to_sync (
            self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'wallet_message',
                'message': message
            }
        )
        
    def wallet_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        }))
