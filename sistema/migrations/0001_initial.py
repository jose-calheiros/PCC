# Generated by Django 4.2.6 on 2024-02-27 11:36

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
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(verbose_name='data')),
                ('members', models.CharField(max_length=400)),
                ('local', models.CharField(max_length=50)),
            ],
        ),
    ]