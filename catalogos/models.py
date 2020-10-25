from django.db import models
from generales.models import ClassModelo

# Create your models here.


class Categoria(ClassModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la categoria',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural = "Categorias"


class SubCategoria(ClassModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Sub Categoría.'
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion, self.descripcion) #salida del formato descripcion

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural = "Sub Categorias"
        unique_together = ('categoria','descripcion')

class Producto(ClassModelo):
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion deL Producto',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion) #salida del formato descripcion

    #SAVE SOBRE ESCRIBE EL VALOR Y LOS PONE EN MAYUSCULA
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Producto, self).save()

    class Meta:
        verbose_name_plural = "Productos"

