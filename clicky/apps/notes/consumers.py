from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from .serializers import NoteSerializer


class NoteConsumer(AsyncJsonWebsocketConsumer):
    group = 'notes_public'

    async def connect(self):
        await self.channel_layer.group_add(
            self.group, self.channel_name
        )

        await self.accept()

    async def receive(self, *args, **kwargs):
        note = await create_note()
        await self.channel_layer.group_send(
            self.group,
            {
                'type': 'create_note',
                'note': note
            }
        )

    async def increment_count(self, event):
        await self.send_json(event['note'])


@database_sync_to_async
def create_note(data):
    serializer = NoteSerializer(data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data
