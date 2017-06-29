from django import forms

from registrar.models import Mamografia
from .models import Persona
# from .models import Encuesta
# from django.db import models
from dal import autocomplete
from .models import Persona, Antecedentes, Mamografia
# class formPaciente(forms.Form):
#
#     cedula_de_identidad = forms.IntegerField()
#     nombre_form = forms.CharField(max_length=100)
#     apellidos = forms.CharField(max_length=100)
#     fecha_nac = forms.DateField()
#     telefono = forms.IntegerField()
#     #actualizado = forms.DateTimeField()


class RegistradoForm(forms.ModelForm):
    class Meta:
        model= Persona
        fields ='__all__'

    def clean_email(self):
       cedula = self.cleaned_data.get("cedula")
       return cedula


class MamografiaForm(forms.ModelForm):
    registrado = forms.ModelChoiceField(
        queryset=Persona.objects.all(),
        widget=autocomplete.ModelSelect2(url='persona-autocomplete')
    )
    class Meta:
        model= Mamografia
        fields = ('__all__')
        # widgets = {
        #     'registrado': autocomplete.ModelSelect2(url='persona-autocomplete')
        # }

class AntecedentesForm(forms.ModelForm):
    registrado = forms.ModelChoiceField(
        queryset=Persona.objects.all(),
        widget=autocomplete.ModelSelect2(url='persona-autocomplete')

    )

    class Meta:
        model= Antecedentes
        fields =('__all__')
        # widgets = {
        #      'registrado': autocomplete.ModelSelect2(url='persona-autocomplete')
        # }
