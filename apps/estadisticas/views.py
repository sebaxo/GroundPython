from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from apps.estadisticas.models import *
from django.views.generic import View, ListView
from django.core import serializers
# Create your views here.


class estadisticas(View):
	def get(self, request):
		#return HttpResponse(data, content_type='aplication/json')
		return render(request, 'contact.html')

class player(ListView):
	def get(self, request, *args, **kwargs):
		name = request.GET.get('name')
		stats = Jugador.objects.filter(nombre='name')

		stat_list = []
		for s in stats:
			info = {
			'nombre': s.name,
			'rango': s.rango,
			'elo': s.elo,
			'partidas_ganadas': s.partidas_ganadas,
			'partidas_perdidas': s.partidas_perdidas,
			}
			stat_list.append(info)
		return JsonResponse(stat_list)