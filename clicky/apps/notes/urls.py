from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.notes_index,
        name='NotesIndex'
    ),
    path(
        'notes-api',
        views.NoteAPI.as_view(),
        name='NotesApi'
    )
]
