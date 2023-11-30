from django.db import models

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

    def __str__(self):
        return f"N. comun: {self.nombre_comun}, N. científico: {self.nombre_cientifico}"

