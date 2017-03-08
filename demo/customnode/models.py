from django.db import models
from viewflow.models import Process

#definimos el modelo de datos
class testProcess(Process):
    text = models.CharField("Nombre", max_length=150)
    email = models.EmailField("Correo Electronico", default="yo@mail.com")
    #date = models.DateField(default=False)
    #date2 = models.DateField(default=False)
    approved = models.BooleanField(default=False)