from django.shortcuts import render
from formulario.forms import LlegarFormu

# Create your views here.

def formulario(request):
    data={
        'form': LlegarFormu
    }
    if request.method == 'POST':
        formulario_lleno=LlegarFormu(data=request.POST)
        if formulario_lleno.is_valid():
            formulario_lleno.save()
            data["mensaje"]= "envio en formulario"
        else:
            data["form"]=formulario_lleno
  
    return render(request,"formulario/formulario.html", data)



