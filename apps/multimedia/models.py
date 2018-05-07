from django.db import models
from datetime import date

# Create your models here.

class foto(models.Model):
	nombre = models.CharField(max_length=40, verbose_name='Nombre', null=False, blank=True)
	img = models.ImageField(verbose_name='Direccion', null=False, blank=False)

	class Meta:
		verbose_name='Foto'
		verbose_name_plural='Fotos'


class video(models.Model):
	nombre = models.CharField(max_length=40, verbose_name='Nombre', null=False, blank=True)
	url = models.CharField(max_length=80, verbose_name='Direccion', null=False, blank=False)

	class Meta:
		verbose_name='Video'
		verbose_name_plural='Videos'


class podcast(models.Model):
	nombre = models.CharField(max_length=40, verbose_name='Nombre', null=False, blank=True)
	url = models.CharField(max_length=80, verbose_name='Direccion', null=False, blank=False)

	class Meta:
		verbose_name='Podcast'
		verbose_name_plural='Podcasts'


class post(models.Model):
	titulo = models.CharField(max_length=60, verbose_name='Titulo', null=False, blank=False)
	contenido = models.TextField(verbose_name='Contenido', null=False, blank=False)
	fecha = models.DateField(default=date.today, verbose_name='Fecha', null=False, blank=False)

	class Meta:
		verbose_name='Post'
		verbose_name_plural='Posts'
		
