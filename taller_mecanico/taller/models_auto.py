# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class Cliente(models.Model):
#     cod_cliente = models.CharField(primary_key=True, max_length=20)
#     dni = models.ForeignKey('Persona', models.DO_NOTHING, db_column='dni')

#     class Meta:
#         managed = False
#         db_table = 'cliente'


# class CustomerDetalle(models.Model):
#     id_detalle_customer = models.IntegerField(primary_key=True)
#     id_customer = models.ForeignKey('CustomerVehiculo', models.DO_NOTHING, db_column='id_customer')
#     cod_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cod_cliente')
#     patente = models.CharField(max_length=10)
#     cod_tipo_vehiculo = models.ForeignKey('TipoVehiculo', models.DO_NOTHING, db_column='cod_tipo_vehiculo')
#     cod_marca = models.ForeignKey('Marca', models.DO_NOTHING, db_column='cod_marca', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'customer_detalle'


# class CustomerVehiculo(models.Model):
#     id_customer = models.AutoField(primary_key=True)
#     cod_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cod_cliente', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'customer_vehiculo'


# class DetalleEmpleadoFechatec(models.Model):
#     id_detalle_empleado_ft = models.AutoField(db_column='id_detalle_empleado_FT', primary_key=True)  # Field name made lowercase.
#     nro_ficha = models.ForeignKey('FichaTecnica', models.DO_NOTHING, db_column='nro_ficha')
#     legajo = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='legajo')
#     horas_trabajadas = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'detalle_empleado_fechatec'


# class DetalleFicha(models.Model):
#     id_detalle_ficha = models.AutoField(primary_key=True)
#     nro_ficha = models.ForeignKey('FichaTecnica', models.DO_NOTHING, db_column='nro_ficha')
#     fecha = models.DateField()
#     cod_repuesto = models.ForeignKey('Repuestos', models.DO_NOTHING, db_column='cod_repuesto')
#     descripcion = models.CharField(max_length=50, blank=True, null=True)
#     cantidad = models.FloatField()
#     precio = models.FloatField()
#     importe = models.FloatField()

#     class Meta:
#         managed = False
#         db_table = 'detalle_ficha'


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'


# class Empleado(models.Model):
#     legajo = models.IntegerField(primary_key=True)
#     dni = models.ForeignKey('Persona', models.DO_NOTHING, db_column='dni')

#     class Meta:
#         managed = False
#         db_table = 'empleado'


# class FichaTecnica(models.Model):
#     nro_ficha = models.IntegerField(primary_key=True)
#     cod_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cod_cliente', blank=True, null=True)
#     vehiculo = models.CharField(max_length=12)
#     subtotal = models.FloatField(blank=True, null=True)
#     mano_obra = models.FloatField(blank=True, null=True)
#     total_general = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'ficha_tecnica'


# class Marca(models.Model):
#     cod_marca = models.AutoField(primary_key=True)
#     nombre = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'marca'


# class Persona(models.Model):
#     dni = models.CharField(primary_key=True, max_length=20)
#     apellido = models.CharField(max_length=40)
#     nombre = models.CharField(max_length=50)
#     direccion = models.CharField(max_length=50, blank=True, null=True)
#     tele_contac = models.CharField(max_length=12, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'persona'


# class Presupuesto(models.Model):
#     nro_presupuesto = models.IntegerField(primary_key=True)
#     cod_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cod_cliente', blank=True, null=True)
#     descripcion = models.CharField(max_length=255, blank=True, null=True)
#     total_presupuesto = models.FloatField(blank=True, null=True)
#     total_gastado = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'presupuesto'


# class Proveedor(models.Model):
#     cod_proveedor = models.CharField(primary_key=True, max_length=20)
#     nombre = models.CharField(max_length=100)
#     direccion = models.CharField(max_length=255, blank=True, null=True)
#     telefono = models.CharField(max_length=20, blank=True, null=True)
#     email = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'proveedor'


# class Repuestos(models.Model):
#     cod_repuesto = models.CharField(primary_key=True, max_length=30)
#     descripcion = models.CharField(max_length=100)
#     pcio_unit = models.FloatField()

#     class Meta:
#         managed = False
#         db_table = 'repuestos'


# class TipoVehiculo(models.Model):
#     cod_tipo_vehiculo = models.CharField(primary_key=True, max_length=5)
#     descripcion = models.CharField(max_length=15, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tipo_vehiculo'


# class Usuario(models.Model):
#     id_usuario = models.AutoField(primary_key=True)
#     username = models.CharField(unique=True, max_length=50)
#     password_hash = models.CharField(max_length=255)
#     rol = models.CharField(max_length=8, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'usuario'
