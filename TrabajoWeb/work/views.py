from django.shortcuts import render
from work.forms import FormWork


# Create your views here.

def work(request):
    form_work=FormWork
    data={
         'form': form_work
    }
    if request.method == 'POST':
        unica=FormWork(data=request.POST)
        if unica.is_valid():
            unica.save()
            return render(request,"formulario/formulario.html")
        else:
            data["form"]=unica

    return render(request,"work/worksample.html",data)