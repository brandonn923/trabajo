from django.db import models
from django.db.models.fields import CharField


# Create your models here.

class PreguntaUnica(models.Model):
    texto=models.CharField(max_length=500)
    
    def __str__(self):
        return self.texto

# desea contestar encuentas

class PreguntasBlog(models.Model):
    nombre=models.CharField(max_length=50,)
    texto=models.TextField(max_length=500,)
    email=models.EmailField()

    def __str__(self):
        return self.nombre

    