from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.click_collector_index,
        name='ClickCollectorIndex'
    ),
    path(
        'create-click/',
        views.create_click,
        name="ClickCollectorCreateClick"
    )
]
