from django.urls import path

from . import consumers

urlpatterns = [
    path(
        'ws/notes/',
        consumers.NoteConsumer.as_asgi(),
        name="WSNotes"
    ),
]
