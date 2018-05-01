from django.db import models

# Create your models here.

class Caster(models.Model):
	nombre = models.CharField(max_length=50)
	partidasGanadas = models.IntegerField()
	partidasPerdidas = models.IntegerField()

class Faccion(models.Model):
	nombre = models.CharField(max_length=50)
	partidasGanadas = models.IntegerField()
	partidasPerdidas = models.IntegerField()
	caster = models.ManyToManyField(Caster)