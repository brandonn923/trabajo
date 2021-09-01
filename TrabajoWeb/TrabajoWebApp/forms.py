from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

class UserRegistarForm(UserCreationForm):
    username=forms.CharField(max_length=150,label='Nombre de Usuario ')
    first_name=forms.CharField(max_length=150,label='Su nombres ')
    last_name=forms.CharField(max_length=150,label='Su Apellidos ')
    email=forms.EmailField()
    password1=forms.CharField(label='Contraseña ',widget=forms.PasswordInput)
    password2=forms.CharField(label='Corfirmar Contraseña ',widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
        help_texts={k:"" for k in fields}