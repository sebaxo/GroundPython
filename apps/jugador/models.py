from django.db import models

# Create your models here.

class Jugador(models.Model):
	nombre = models.CharField(max_length=50)
	rango = models.IntegerField()
	elo = models.IntegerField()
	partidasGanadas = models.IntegerField()
	partidasPerdidas = models.IntegerField()