from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from apps.estadisticas.models import Jugador, Faccion, Caster
from django.views.generic import View, ListView
from django.core import serializers


class estadisticas(View):
	def get(self, request):
		return render(request, 'contact.html')

class home(View):
	def get(self, request):
		return render(request, 'index.html')

class multimedia(View):
	def get(self, request):
		return render(request, 'multimedia.html')

class player(ListView):
	def get(self, request, name):
		if name == 'all':	
			stats = Jugador.objects.all()
		else:
			stats = Jugador.objects.filter(nombre=name)

		stat_list = []
		for s in stats:
			info = {
			'nombre': s.nombre,
			'rango': s.rango,
			'elo': s.elo,
			'partidas_ganadas': s.partidas_ganadas,
			'partidas_perdidas': s.partidas_perdidas,
			}
			stat_list.append(info)
		return JsonResponse(stat_list, safe=False)

class faction(ListView):
	def get(self, request, name):
		if name == 'all':
			factions = Faccion.objects.all()
		else:
			factions = Faccion.objects.filter(nombre=name)

		faction_list = []
		for f in factions:
			info = {
			'nombre': f.nombre,
			'partidas_ganadas': f.partidas_ganadas,
			'partidas_perdidas': f.partidas_perdidas,
			}
			faction_list.append(info)
		return JsonResponse(faction_list, safe=False)

class caster(ListView):
	def get(self, request, name):
		if name == 'all':
			casters = Caster.objects.all()
		else:
			casters = Caster.objects.filter(nombre=name)

		caster_list = []
		for c in casters:
			info = {
			'nombre': c.nombre,
			'partidas_ganadas': c.partidas_ganadas,
			'partidas_perdidas': c.partidas_perdidas,
			}
			caster_list.append(info)
		return JsonResponse(caster_list, safe=False)