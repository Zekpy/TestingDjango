from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen_url = models.URLField(max_length=500, blank=True)  # Campo de texto para la URL de la imagen

    def __str__(self):
        return self.nombre
