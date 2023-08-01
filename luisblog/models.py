from django.db import models

# Create your models here.

class Blog(models.Model):

    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)

    