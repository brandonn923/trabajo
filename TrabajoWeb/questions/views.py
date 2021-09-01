from django.shortcuts import render
from questions.forms import QuestionS, AnswerS
# Create your views here.

def questio(request):
    llenar_answer=AnswerS
    llenar_question=QuestionS
    data={
         'form': llenar_question
    }
    if request.method == 'POST':
        unica=QuestionS(data=request.POST)
        if unica.is_valid():
            unica.save()
            data["mensaje"]= "envio en question"
        else:
            data["form"]=unica

    return render(request,"questions/question.html",data)



def answer(request):
    llenar_answer=AnswerS
    data={
         'form': llenar_answer
    }
    if request.method == 'POST':
        unica=AnswerS(data=request.POST)
        if unica.is_valid():
            unica.save()
            data["mensaje"]= "envio en answer"
        else:
            data["form"]=unica
    return render(request,"questions/answer.html",data )