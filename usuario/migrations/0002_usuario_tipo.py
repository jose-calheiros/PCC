# Generated by Django 5.0.4 on 2024-05-20 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tipo',
            field=models.CharField(choices=[('professor', 'Professor'), ('aluno', 'Aluno')], default='aluno', max_length=10, verbose_name='Tipo de Usuário'),
        ),
    ]
