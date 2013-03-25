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


class MateUpdateForm(ModelForm):
    class Meta:
        model = Mate
        exclude = ('color',)


class MateForm(ModelForm):
    class Meta:
        model = Mate


class BombillaForm(ModelForm):
    class Meta:
        model = Bombilla


class PrestamoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(PrestamoForm, self).__init__(*args, **kwargs)  # populates post
#        if self.instance:
        self.fields['mate'].queryset = Mate.objects.filter(disponible=True)
        self.fields['termo'].queryset = Termo.objects.filter(disponible=True)
        self.fields['bombilla'].queryset = Bombilla.objects.filter(
            disponible=True)

    class Meta:
        model = Prestamo
#      mate = forms.ModelChoices(queryset=Mate.objects.filter(disponible=True))
        exclude = ('cliente',
                    'fecha',
                    'devuelto',
                    'fecha_devolucion',)
