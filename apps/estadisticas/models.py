from django.db import models

# Create your models here.

class Caster(models.Model):
	nombre = models.CharField(max_length=50, verbose_name='Nombre', blank=False, null=False)
	partidas_ganadas = models.PositiveIntegerField(verbose_name='Partidas Ganadas', blank=False, null=False)
	partidas_perdidas = models.PositiveIntegerField(verbose_name='Partidas Perdidas', blank=False, null=False)

	class Meta:
		verbose_name='Caster'
		verbose_name_plural='Casters'


class Faccion(models.Model):
	nombre = models.CharField(max_length=50)
	partidas_ganadas = models.PositiveIntegerField(verbose_name='Partidas Ganadas', blank=False, null=False)
	partidas_perdidas = models.PositiveIntegerField(verbose_name='Partidas Perdidas', blank=False, null=False)
	caster = models.ManyToManyField(Caster)

	class Meta:
		verbose_name='Faccion'
		verbose_name_plural='Facciones'


class Jugador(models.Model):
	nombre = models.CharField(max_length=50, verbose_name='Nombre', blank=False, null=False)
	rango = models.PositiveIntegerField(verbose_name='Rango', blank=False, null=False)
	elo = models.PositiveIntegerField(verbose_name='Elo', blank=False, null=False)
	partidas_ganadas = models.PositiveIntegerField(verbose_name='Partidas Ganadas', blank=False, null=False)
	partidas_perdidas = models.PositiveIntegerField(verbose_name='Partidas Perdidas', blank=False, null=False)

	class Meta:
		verbose_name='Jugador'
		verbose_name_plural='Jugadores'


class Partida(models.Model):
	jugador1 = models.ForeignKey(Jugador, null=False, related_name='winner_player',blank=False, on_delete=models.CASCADE)
	jugador2 = models.ForeignKey(Jugador, null=False, related_name='looser_player',blank=False, on_delete=models.CASCADE)
	faccion1 = models.ForeignKey(Faccion, null=False, related_name='winner_facction',blank=False, on_delete=models.CASCADE)
	faccion2 = models.ForeignKey(Faccion, null=False, related_name='looser_facction',blank=False, on_delete=models.CASCADE)
	caster1 = models.ForeignKey(Caster, null=False, related_name='winner_caster',blank=False, on_delete=models.CASCADE)
	caster2 = models.ForeignKey(Caster, null=False, related_name='looser_caster',blank=False, on_delete=models.CASCADE)

	class Meta:
		verbose_name='Partida'
		verbose_name_plural='Partidas' 