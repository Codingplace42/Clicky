from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.click_collector_index,
        name='ClickCollectorIndex'
    ),
    path(
        'clickapi/',
        views.ClickAPI.as_view(),
        name="ClickCollectorAPI",
    )
]
