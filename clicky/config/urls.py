from django.urls import path, include

urlpatterns = [
    path('', include('click_collector.urls')),
    path('notes/', include('notes.urls')),
]
