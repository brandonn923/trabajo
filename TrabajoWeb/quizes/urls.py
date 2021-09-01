
from django.urls import path
from .views import (
    QuizListView , 
    quiz_view,  
    quiz_data_view,
    save_quiz_view,
     
    )
from . import views



urlpatterns = [
    path('', QuizListView.as_view(), name='quizes'),   
    path('llenar/',views.llenar, name="llenar"),
    path('<pk>/', quiz_view, name='quiz-view'),   
    path('<pk>/save/', save_quiz_view, name='save-view'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
     

]