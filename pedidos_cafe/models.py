from django.db import models
class PedidoCafe(models.Model):
     cliente = models.CharField(max_length=100)
     tipo_base = models.CharField(
         max_length=20,
         choices=[
             ("espresso", "Espresso"),
             ("americano", "Americano"),
             ("latte", "Latte"),
         ],
     )
     ingredientes = models.JSONField(default=list)
     tamanio = models.CharField(
         max_length=10,
         choices=[
             ("pequenio", "Pequeño"),
             ("mediano", "Mediano"),
             ("grande", "Grande"),
         ],
     )
     fecha = models.DateTimeField(auto_now_add=True)
# Create your models here.
