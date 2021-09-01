from django.urls import path
from . import views

urlpatterns = [
   
    path('pregunta/',views.pregunta, name="pregunta"),
    path('preguntasmulti/',views.preguntaMulti, name="preguntasmulti"),
    path('blockPregunta/',views.blogPregunta, name="blockPregunta"),

]