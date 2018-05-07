from django.contrib import admin
from apps.estadisticas.models import *

# Register your models here.

class JugadorAdmin(admin.ModelAdmin):
	pass


class PartidaAdmin(admin.ModelAdmin):
	pass


class FaccionAdmin(admin.ModelAdmin):
	pass


class CasterAdmin(admin.ModelAdmin):
	pass


admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Partida, PartidaAdmin)
admin.site.register(Faccion, FaccionAdmin)
admin.site.register(Caster, CasterAdmin)