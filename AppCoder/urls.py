from django.contrib import admin
from django.urls import path
from AppCoder.views import home, sobre_mi, comentario_planta, busqueda_planta, crear_planta_form, crear_usuario_form, crear_especialista_form, PlantaList, PlantaDetalle, PlantaCreacion, PlantaActualizacion, PlantaEliminar

urlpatterns = [
    path('plantas/listar', PlantaList.as_view(), name="PlantasList"),
    path('planta/<int:pk>', PlantaDetalle.as_view(), name="PlantasDetail"),
    path('planta/', crear_planta_form),
    path('buscar_planta/', busqueda_planta),
    path('usuario/', crear_usuario_form),
    path('especialista/', crear_especialista_form),
    path('crear/', PlantaCreacion.as_view(), name="PlantaCreate"),
    path('editar/<int:pk>', PlantaActualizacion.as_view(), name="PlantaUpdate"),
    path('eliminar/<int:pk>', PlantaEliminar.as_view(), name="PlantaDelete"),
    path('home/', home),
    path('comentarios/<int:pk>/',comentario_planta , name="Comentarios"),
    path('sobre_mi/', sobre_mi, name="SobreMi"),
]
