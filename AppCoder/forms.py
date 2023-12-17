from django import forms
from AppCoder.models import Planta, Comentario

class PlantaForm(forms.Form):
    class Meta:
        model = Planta
        fields = ['nombre_comun', 'nombre_cientifico', 'imagen']

class BusquedaPlantaForm(forms.Form):
    nombre_comun = forms.CharField()

class UsuarioForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()

class EspecialistaForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()     

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['cuerpo']
