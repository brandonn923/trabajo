from django import forms
from .models import Formulario

class LlegarFormu(forms.ModelForm):

    class Meta:
        model=Formulario
        fields='__all__'
