
from django.urls import path
from apps.jugador.views import index

urlpatterns = [
    path('', index)
]
