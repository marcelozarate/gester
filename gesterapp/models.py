# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Facultad(models.Model):
    nombre = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Facultades'

    def __unicode__(self):
        return self.nombre


class Carrera(models.Model):
    nombre = models.CharField(max_length=128)
    facultad = models.ForeignKey(Facultad, null=False, blank=False)

    def __unicode__(self):
        return self.nombre


COLOR_CHOICES = (
        (u'RO', u'Rojo'),
        (u'MA', u'Marrón'),
        (u'BL', u'Blanco'),
        (u'AM', u'Amarillo'),
        (u'NA', u'Naranja'),
        (u'RS', u'Rosa'),
        (u'VI', u'Violeta'),
        (u'AZ', u'Azul'),
        (u'VE', u'Verde'),
        (u'GR', u'Gris'),
        (u'NE', u'Negro'),
    )


class Mate(models.Model):
    color = models.CharField(max_length=2,
        choices=COLOR_CHOICES, default=u'RO')
    disponible = models.BooleanField(default=True)

    def __unicode__(self):
        return self.color


class Termo(models.Model):
    color = models.CharField(max_length=2,
        choices=COLOR_CHOICES, default=u'NA')
    disponible = models.BooleanField(default=True)

    def __unicode__(self):
        return self.color


TIPOBOMBI_CHOICES = (
        (u'C', u'Clásica'),
        (u'R', u'Resorte'),
    )


class Bombilla(models.Model):
    tipo = models.CharField(max_length=1,
        choices=TIPOBOMBI_CHOICES, default=u'C')
    disponible = models.BooleanField(default=True)

    def __unicode__(self):
        return self.tipo


class Usuario(models.Model):
    nombre = models.CharField(max_length=128)
    facultad = models.ForeignKey(Facultad, null=False, blank=False)
    carrera = models.ForeignKey(Carrera, null=False, blank=False)
    dni = models.PositiveIntegerField(unique=True)
    direccion = models.CharField(max_length=128)
    telefono = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)
    fechaingreso = models.DateTimeField(null=False, blank=False)
    creadopor = models.ForeignKey(User, default=0)

    def __unicode__(self):
        return self.nombre


class Prestamo(models.Model):
    cliente = models.ForeignKey(Usuario, null=False, blank=False)
    mate = models.ForeignKey(Mate, null=True, blank=True)
    termo = models.ForeignKey(Termo, null=True, blank=True)
    bombilla = models.ForeignKey(Bombilla, null=True, blank=True)
    fecha = models.DateTimeField(null=False, blank=False)
    devuelto = models.BooleanField(default=False)
    fecha_devolucion = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return str(self.pk)
