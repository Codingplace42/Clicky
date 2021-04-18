from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from .serializers import ClickSerializer


class ClickConsumer(AsyncJsonWebsocketConsumer):
    group = 'public'

    async def connect(self):
        await self.channel_layer.group_add(
            self.group, self.channel_name
        )

        await self.accept()

    async def receive(self, *args, **kwargs):
        click = await create_click()
        await self.channel_layer.group_send(
            self.group,
            {
                'type': 'increment_count',
                'click': click
            }
        )

    async def increment_count(self, event):
        await self.send_json(event['click'])


@database_sync_to_async
def create_click():
    serializer = ClickSerializer(data={})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data
