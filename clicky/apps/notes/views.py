from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Note
from .serializers import NoteSerializer
from rest_framework.pagination import PageNumberPagination


def notes_index(request):
    return render(request, 'notes/index.html')


class NotePagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 100


class NoteAPI(ListAPIView):
    queryset = Note.objects
    serializer_class = NoteSerializer
    pagination_class = NotePagination
