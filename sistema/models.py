from django.db import models

class Experimento(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField("data")
    members = models.CharField(max_length=400)
    local = models.CharField(max_length=50)



    def __str__(self):
        return self.name