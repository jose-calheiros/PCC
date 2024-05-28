from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    
    TIPO_USUARIO_CHOICES = (
        ('professor', 'Professor'),
        ('aluno', 'Aluno'),
    )
    
    tipo = models.CharField(
        max_length=10,
        choices=TIPO_USUARIO_CHOICES,
        default='aluno',
        verbose_name='Tipo de Usuário'
    )


    def clean_tipo(self):
        return self
    

    # def save(self):
    #     user.set_password(self.password)
