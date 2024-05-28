from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioForms(UserCreationForm):

    TIPO_CHOICES = [
        ('professor', 'Professor'),
        ('aluno', 'Aluno'),
    ]
    tipo = forms.ChoiceField(choices=TIPO_CHOICES)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'tipo', 'password']