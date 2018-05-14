from django.urls import path, include
from apps.estadisticas.views import *

urlpatterns=[
	path('estadisticas/', estadisticas.as_view(), name='estadisticas'),
	path('player/<name>', player.as_view(), name='player'),
]