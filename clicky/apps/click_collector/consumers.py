from channels.generic.websocket import AsyncWebsocketConsumer


class ClickConsumer(AsyncWebsocketConsumer):
    async def receive(self, text_data=None, bytes_data=None):
        print("RECEIVED")
