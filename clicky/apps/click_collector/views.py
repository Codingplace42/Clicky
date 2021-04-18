from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Click


def click_collector_index(request):
    context = {
        'clicks': Click.objects.order_by('-timestamp')[:5]
    }
    return render(request, 'collector/index.html', context)


@require_http_methods(["POST", ])
def create_click(request):
    Click.objects.create()
    return redirect("ClickCollectorIndex")
