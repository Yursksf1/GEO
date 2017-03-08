from django.db import models
from viewflow.models import Process

#definimos el modelo de datos
class ambProcess(Process):
    text = models.CharField(max_length=150)
    email = models.EmailField(default=False)
    approved = models.BooleanField(default=False)