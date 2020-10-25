from django.db import models

# Create your models here.


class ClassModelo(models.Model):
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True) # FECHA DEL SERVIDOR
    modificado = models.DateTimeField(auto_now= True) # FECHA DE LA MODIFICACION

    class Meta:
        abstract = True # con esa instruccion el modelo  de db no se crea en la base de datos
