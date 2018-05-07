from django.urls import path, include
from apps.estadisticas.views import *

urlpatterns=[
	path('', estadisticas.as_view(), name='estadisticas'),
	path('player', player.as_view(), name='player'),
]