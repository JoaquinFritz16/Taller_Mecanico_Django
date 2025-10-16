from django.db import models

class Persona(models.Model):
    dni = models.CharField(max_length=20, primary_key=True)
    apellido = models.CharField(max_length=40)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    tele_contac = models.CharField(max_length=12, blank=True, null=True)

class Cliente(models.Model):
    cod_cliente = models.CharField(max_length=20, primary_key=True)
    dni = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='dni')

class Empleado(models.Model):
    legajo = models.IntegerField(primary_key=True)
    dni = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='dni')

class TipoVehiculo(models.Model):
    cod_tipo_vehiculo = models.CharField(max_length=5, primary_key=True)
    descripcion = models.CharField(max_length=15, blank=True, null=True)

class Marca(models.Model):
    cod_marca = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password_hash = models.CharField(max_length=255)
    rol = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('empleado', 'Empleado')], default='empleado')

class Proveedor(models.Model):
    cod_proveedor = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

class Repuesto(models.Model):
    cod_repuesto = models.CharField(max_length=30, primary_key=True)
    descripcion = models.CharField(max_length=100)
    pcio_unit = models.FloatField()

class FichaTecnica(models.Model):
    nro_ficha = models.IntegerField(primary_key=True)
    cod_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='cod_cliente', blank=True, null=True)
    vehiculo = models.CharField(max_length=12)
    subtotal = models.FloatField(blank=True, null=True)
    mano_obra = models.FloatField(blank=True, null=True)
    total_general = models.FloatField(blank=True, null=True)

class Presupuesto(models.Model):
    nro_presupuesto = models.IntegerField(primary_key=True)
    cod_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='cod_cliente', blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    total_presupuesto = models.FloatField(blank=True, null=True)
    total_gastado = models.FloatField(blank=True, null=True)
