from django import forms
from django.shortcuts import render
from pregunta.forms import UnicaPregunta, BlogPregunta
from pregunta.models import PreguntasBlog


# Create your views here.


def pregunta(request):
    preguntas=UnicaPregunta
    data={
         'form': preguntas
    }
    if request.method == 'POST':
        unica=UnicaPregunta(data=request.POST)
        if unica.is_valid():
            unica.save()
            return render(request,"formulario/formulario.html")
        else:
            data["form"]=unica
    return render(request,"pregunta/pregunta.html",data)

def preguntaMulti(request):
    preguntas=BlogPregunta
    data={
         'form': preguntas
    }
    if request.method == 'POST':
        unica=BlogPregunta(data=request.POST)
        if unica.is_valid():
            unica.save()
            return render(request,"formulario/formulario.html")
        else:
            data["form"]=unica
    return render(request,"pregunta/preguntasMulti.html",data)


def blogPregunta(request):
    block=PreguntasBlog.objects.all()
    return render(request,"pregunta/blockPregunta.html",{'block':block})

































# def countries_view(request):
#     paises=CountryForm
#     data={
#         'form':paises 
#     }
#     if request.method == 'POST':
#         form = CountryForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request,"formulario/formulario.html")
#         else:
#             data["form"]=form
#     else:
#         form = CountryForm

#     return render(request,"pregunta/preguntasMulti.html",data )

