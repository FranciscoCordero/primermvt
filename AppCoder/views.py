from django.shortcuts import render
from AppCoder.models import Madre, Padre, Hermano
from django.http import HttpResponse
from django.template import Context, Template

# Create your views here.
def familia(self):

    madre = Madre(nombre = "Laura", dni = 23541670, fecha_nacimiento ="12/08/1973")
    madre.save()
    padre = Padre(nombre = "Roberto", dni = 25971910, fecha_nacimiento ="20/11/1975")
    padre.save()
    hermano = Hermano(nombre = "Juani", dni = 44971235, fecha_nacimiento ="20/01/2002")
    hermano.save()

    diccionario = {
        "mnombre":madre.nombre, "mdni":madre.dni, "mfechanacimiento":madre.fecha_nacimiento,
        "pnombre":padre.nombre, "pdni":padre.dni, "pfechanacimiento":padre.fecha_nacimiento,
        "hnombre":hermano.nombre, "hdni":hermano.dni, "hfechanacimiento":hermano.fecha_nacimiento,
    }
    
    miHtml= open("C:/Users/Usuario/Desktop/python/ProyectoCoder/template/template1.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    contexto = Context(diccionario)

    document = plantilla.render(contexto)

    return HttpResponse(document)