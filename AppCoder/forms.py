from django import forms

class PlantaForm(forms.Form):
    nombre_comun = forms.CharField()
    nombre_cientifico = forms.CharField()

class BusquedaPlantaForm(forms.Form):
    nombre_comun = forms.CharField()

class UsuarioForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()

class EspecialistaForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()     