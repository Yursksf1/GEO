from django.db import models
from viewflow.models import Process

#definimos el modelo de datos
class ambProcess(Process):
    text = models.CharField(max_length=150)
    text2 = models.CharField(max_length=150)
    approved = models.BooleanField(default=False)