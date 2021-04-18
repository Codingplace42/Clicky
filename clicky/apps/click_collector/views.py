from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Click
from .serializers import ClickSerializer


def click_collector_index(request):
    return render(request, 'collector/index.html')


class ClickAPI(ListCreateAPIView):
    queryset = Click.objects.order_by('-timestamp')[:5]
    serializer_class = ClickSerializer
