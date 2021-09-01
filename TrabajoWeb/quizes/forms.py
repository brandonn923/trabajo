from django import forms
from django.forms import widgets
from .models import Quiz


class QuizPregunta(forms.ModelForm):

    class Meta:
        model=Quiz
        fields='__all__'
        labels={
            'name': 'Titulo del preguntas',
            'topic': 'tipo de preguntas',
            'number_of_questions': 'numeros de respuestas',
            
        }
        widgets={
            'name': widgets.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Escriba la pregunta',

                }
            ),

            'topic': widgets.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese tipo de pregunta',
                    
                }
            ),
            'number_of_questions': widgets.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese numero las respuesta',
                    
                    
                }
            ),
        }


 

































# class CountryForm(forms.Form):
#         class Meta:
#                 models=CargarP
#                 fields='__all__'

#         OPTIONS = (
#                 ("AUT", "Austria"),
#                 ("DEU", "Germany"),
#                 ("NLD", "Neitherlands"),
#                 )
#         Countries = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
#                                              choices=OPTIONS)