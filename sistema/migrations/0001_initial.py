# Generated by Django 5.0.4 on 2024-05-20 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('n_maquina', models.CharField(max_length=30)),
                ('resultado', models.CharField(max_length=50)),
                ('localização', models.CharField(max_length=50)),
            ],
        ),
    ]
