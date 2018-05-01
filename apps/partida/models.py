from django.db import models
from apps.jugador.models import Jugador
from apps.faccion.models import *

# Create your models here.

class Partida(models.Model):
	jugador1 = models.ForeignKey(Jugador, null=False, related_name='winner_player',blank=False, on_delete=models.CASCADE)
	jugador2 = models.ForeignKey(Jugador, null=False, related_name='looser_player',blank=False, on_delete=models.CASCADE)
	faccion1 = models.ForeignKey(Faccion, null=False, related_name='winner_facction',blank=False, on_delete=models.CASCADE)
	faccion2 = models.ForeignKey(Faccion, null=False, related_name='looser_facction',blank=False, on_delete=models.CASCADE)
	caster1 = models.ForeignKey(Caster, null=False, related_name='winner_caster',blank=False, on_delete=models.CASCADE)
	caster2 = models.ForeignKey(Caster, null=False, related_name='looser_caster',blank=False, on_delete=models.CASCADE)