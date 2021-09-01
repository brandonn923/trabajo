from django.db import models

# Create your models here.




class PreguntaMotivacional(models.Model):
    pregunta=models.CharField(max_length=250)
    contenido=models.TextField(max_length=500)

    def __str__(self):
        return self.pregunta

class Worksample(models.Model):
    titulo=models.CharField(max_length=250)
    mensaje=models.TextField()
    pregunta_mol=models.ForeignKey(PreguntaMotivacional, related_name='opcional', on_delete=models.CASCADE)
    caso=models.TextField()
    final_men=models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.titulo