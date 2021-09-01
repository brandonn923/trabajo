from django import forms
from django.forms import widgets
from .models import Question, Answer


class QuestionS(forms.ModelForm):

    class Meta:
        model=Question
        fields='__all__'
        labels={
            'text': 'Respuesta',
            'quiz pregunta': 'elegir',
        }
        widgets={
            'text': widgets.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Escriba la respuesta',

                }
            ),
        'quiz': widgets.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Eliga la Pregunta',
                    
                }
            ),
        }

class AnswerS(forms.ModelForm):

    class Meta:
        model=Answer
        fields='__all__'
        labels={
            'text': 'Escribir la respuesta correcta',
            'correct': 'elegir ',
            'question': 'Elegir respuesta',
        }
        widgets={
            'text': widgets.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Escriba la respuesta',

                }
            ),
            'quiz': widgets.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Eliga la Pregunta',
                    
                }
            ),
            'question': widgets.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Eliga la Pregunta',
                    
                }
            ),
        }
