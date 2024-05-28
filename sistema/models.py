from django.db import models
from django.contrib.auth import get_user_model

class Experimento(models.Model):
    nome = models.CharField(max_length=100)
    n_maquina = models.CharField(max_length=30,)
    participantes = models.ForeignKey(get_user_model(),                             
                                      on_delete=models.CASCADE,
                                      limit_choices_to={'tipo': 'aluno'},
                                      blank=True,)
    resultado = models.CharField(max_length=50)
    localização = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

