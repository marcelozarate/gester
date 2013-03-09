# -*- coding: utf-8 *-*
from gesterapp.models import Usuario, Termo, Mate, Bombilla, Prestamo
from django.forms import ModelForm


class UserForm(ModelForm):
    class Meta:
        model = Usuario
        exclude = ('fechaingreso',
                    'creadopor',)


class TermoForm(ModelForm):
    class Meta:
        model = Termo


class MateForm(ModelForm):
    class Meta:
        model = Mate


class BombillaForm(ModelForm):
    class Meta:
        model = Bombilla


class PrestamoForm(ModelForm):
    class Meta:
        model = Prestamo
        exclude = ('cliente',
                    'fecha',
                    'devuelto',
                    'fecha_devolucion',)
