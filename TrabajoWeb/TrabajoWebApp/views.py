from django.shortcuts import render 
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistarForm
from django.contrib import messages
from formulario.models import Ofertas 

# Create your views here.

def index(request):
    oferta=Ofertas.objects.all()
    return render(request,"TrabajoWebApp/index.html",{'oferta':oferta})

def registar(request):
    if request.method =='POST':
        form=UserRegistarForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
    else:
        form=UserRegistarForm()
    context={'form': form}
    return render(request,"TrabajoWebApp/registar.html",context)

