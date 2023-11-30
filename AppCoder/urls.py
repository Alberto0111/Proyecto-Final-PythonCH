from django.contrib import admin
from django.urls import path
from AppCoder.views import busqueda_planta, crear_planta_form, mostrar_plantas, crear_usuario_form, crear_especialista_form

urlpatterns = [
    path('plantas/', mostrar_plantas),
    path('planta/', crear_planta_form),
    path('buscar_planta/', busqueda_planta),
    path('usuario/', crear_usuario_form),
    path('especialista/', crear_especialista_form),
]
