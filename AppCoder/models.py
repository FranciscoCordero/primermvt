from django.db import models

# Create your models here.
class Madre(models.Model):

    nombre = models.CharField(max_length=40)
    dni = models.IntegerField()
    fecha_nacimiento = models.CharField(max_length=50)

class Padre(models.Model):

    nombre = models.CharField(max_length=40)
    dni = models.IntegerField()
    fecha_nacimiento = models.CharField(max_length=50)

class Hermano(models.Model):

    nombre = models.CharField(max_length=40)
    dni = models.IntegerField()
    fecha_nacimiento = models.CharField(max_length=50)