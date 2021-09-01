from django import forms
from .models import PreguntaUnica,PreguntasBlog

class UnicaPregunta(forms.ModelForm):

    class Meta:
        model=PreguntaUnica
        fields='__all__'

class BlogPregunta(forms.ModelForm):

    class Meta:
        model=PreguntasBlog
        fields='__all__'




































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