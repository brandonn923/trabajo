from django.urls import path
from questions import views

urlpatterns = [
   
    path('questions/',views.questio, name="questions"),
    path('answer/',views.answer, name="answer"),

]