from django.db import models

# Create your models here.

class Cargo(models.Model):
    texto=models.TextField(verbose_name='cargo')

    def __str__(self):
        return self.texto

class Ofertas(models.Model):
    titulo=models.CharField(max_length=60)
    texto=models.TextField(max_length=200)
    imagan=models.ImageField(upload_to='formulario')
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

opciones=[
    [0, "Si"],
    [1, "No"],
    
]


class Formulario(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    edad=models.CharField(max_length=2)
    telefono=models.CharField(max_length=10)
    correo=models.EmailField()
    vacante=models.ForeignKey(Ofertas, related_name='cargo', on_delete=models.CASCADE)
    profeccion=models.CharField(max_length=40)
    trabaja_actual=models.IntegerField(choices=opciones)
    
    def __str__(self):
        return self.nombre