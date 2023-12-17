from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}"


class Especialista(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}, contacto: {self.email}"

class Planta(models.Model):
    nombre_comun = models.CharField(max_length=30)
    nombre_cientifico = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to="plantas", null=True, blank=True)

    def __str__(self):
        return f"N. comun: {self.nombre_comun}, N. científico: {self.nombre_cientifico}"

class Comentario(models.Model):
    cuerpo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE, related_name="comentarios")
    
    def __str__(self):
        return f'Comentario de {self.usuario.username} en {self.planta.nombre_comun}'