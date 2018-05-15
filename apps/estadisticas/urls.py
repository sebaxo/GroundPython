from django.urls import path, include
from apps.estadisticas.views import *

urlpatterns=[
	path('estadisticas/', estadisticas.as_view(), name='estadisticas'),
	path('estadisticas/player/<name>', player.as_view(), name='player'),
	path('estadisticas/faction/<name>', faction.as_view(), name='faction'),
	path('estadisticas/caster/<name>', caster.as_view(), name='caster'),
	path('multimedia/', multimedia.as_view(), name='multimedia'),
	path('', home.as_view(), name='home'),
]