from django import forms
from django.forms import widgets
from.models import Worksample

class FormWork(forms.ModelForm):
    
    class Meta:
        model=Worksample
        fields='__all__'
        labels={
            'name': 'Titulo del Work Sample',
            'topic': 'Bienvenida: introducción al work sample',
            'number_of_questions': 'Preguntas de motivación',
            'caso': 'caso de negocio',
            'final_men': 'Mensaje Final',
        }
        widgets={
            'titulo': widgets.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese titulo',

                }
            ),

            'mensaje': widgets.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese Mensaje',
                    'rows': 5,
                    'cols': 3
                    
                }
            ),
            'pregunta_mol': widgets.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Pregunta',
                    
                }
            ),
             'caso': widgets.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Escriba el caso de negocio',
                    'rows': 6,
                    'cols': 3
                    
                }
            ),
             'final_men': widgets.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Escriba mensaje final',
                    'rows': 8,
                    'cols': 3
                    
                }
            ),
            

        }
 



   
