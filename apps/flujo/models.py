from django.db import models

from apps.flujo import properties


class Moneda(models.Model):
    pais = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)

#, blank=True, null=True, default=""
class ActivoCaja(models.Model):
    nombre_Activo = models.CharField(max_length=255)
    valor_activo = models.DecimalField(decimal_places=2)
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE())
    tiempo = models.CharField(max_length=30, choices=properties.TIPO_TIEMPO)
    valor_tiempo = models.PositiveIntegerField()


class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=100)


class Obligaciones(models.Model):
    nombre = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    falta_pagar_dinero = models.DecimalField(decimal_places=2)
    falta_pagar_dias = models.CharField(max_length=30, choices=properties.TIPO_TIEMPO)
    valor_tiempo = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=250)
    tasa = models.DecimalField(decimal_places=2)


