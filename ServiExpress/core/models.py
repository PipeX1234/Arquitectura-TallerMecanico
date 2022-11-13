from asyncio.windows_events import NULL
from distutils.command.upload import upload
from email.policy import default
from pickle import TRUE
from sre_parse import Verbose
from tabnanny import verbose
from tkinter import CASCADE
from django.contrib.auth.models import User
from django.db import models
from django.forms import IntegerField

# Create your models here.

class SucursalProveedor(models.Model):
    idSucursalProveedor = models.IntegerField(primary_key=True, verbose_name="Id")
    region = models.CharField(max_length=50, blank=False, null=False, verbose_name="Region")
    comuna = models.CharField(max_length=50, blank=False, null=False, verbose_name="Comuna")

    def __str__(self):
        return self.region + " " + self.comuna

class Proveedor(models.Model):
    idProveedor = models.IntegerField(primary_key=True, verbose_name="Id del producto") 
    idSucursalProveedor = models.ForeignKey(SucursalProveedor, on_delete=models.DO_NOTHING)
    nombreProveedor = models.CharField(max_length=160, blank=False, null=False, verbose_name="Region")
    correoProveedor = models.CharField(max_length=100, null=False, blank=False, verbose_name="Correo Proveedor")
    telefonoProveedor = models.IntegerField(blank=False, null=False, verbose_name="Precio Producto")

    def __str__(self):
        return self.nombreProveedor

class EstadoOrden(models.Model):
    idEstado = models.IntegerField(primary_key=True, verbose_name="Estado Orden de Pedido")
    nombreEstado = models.CharField(max_length=50, blank=False, null=False, verbose_name="Estado Orden de Pedido")

    def __str__(self):
        return self.nombreEstado

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="ID del Producto")
    nombreProducto = models.CharField(null=False, blank=False, verbose_name="Nombre del Producto")
    precioProducto = models.IntegerField(null=False, blank=False, verbose_name="Precio del Producto")
    cantStockProd = models.IntegerField(null=False, blank=False, verbose_name="Stock del Producto")

    def __str__(self):
        return self.nombreProducto
    
class OrdenDePedido(models.Model):
    idOrdenPedido = models.IntegerField(primary_key=True, verbose_name="ID orden de pedido")
    idEstado = models.ForeignKey(EstadoOrden, on_delete=models.DO_NOTHING)
    fecha = models.DateField(null=False, blank=False, verbose_name="Fecha de la Orden")
    precioFinal = models.IntegerField(null=False, blank=False, verbose_name="Precio de la Orden de Pedido")

    def __str__(self):
        return str(self.idOrdenPedido)

class DetalleOrden(models.Model):
    idDetalleOrden = models.IntegerField(primary_key=True, verbose_name="Id Detalle de Orden de Pedido")
    idProducto = models.ForeignKey(Producto, verbose_name="Producto Seleccionado")
    idOrdenPedido = models.ForeignKey(OrdenDePedido, verbose_name="Orden De Pedido")

    def __str__(self):
        return str(self.idDetalleOrden)

class TipoServicio(models.Model):
    idTipoServicio = models.IntegerField(primary_key=True, verbose_name="ID Tipo Servicio")
    descTipoServicio = models.CharField(max_length=50, null=False, blank=False, verbose_name="Descripción del Tipo de Servicio")

    def __str__(self):
        return self.descTipoServicio

class Servicio(models.Model):
    idServicio = models.IntegerField(primary_key=True, verbose_name="Id del Servicio")
    idProducto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
    tipoServicio = models.ForeignKey(TipoServicio, on_delete=models.DO_NOTHING)
    nombreServicio = models.CharField(max_length=50, blank=False, null=False, verbose_name="Nombre del Servicio")
    precioServicio = models.IntegerField(blank=False, null=False, verbose_name="Precio del Servicio")
    descrpServicio = models.CharField(max_length=300, blank=False, null=False, verbose_name="Descripción del Servicio")

    def __str__(self):
        return self.nombreServicio

class PerfilCliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    runCliente = models.IntegerField(primary_key=True, verbose_name="Run sin puntos")
    dvrunCliente = models.CharField(max_length=1, min_lenght=1, blank=False, null=False, verbose_name="-")
    sNombreCliente = models.CharField(max_length=50, blank=False, null=False, verbose_name="Segundo Nombre")
    apMaternoCliente = models.CharField(max_length=50, blank=False, null=False, verbose_name="Apellido Materno")
    fechNacimCliente = models.DateField(null=False, blank=False, verbose_name="Fecha de Nacimiento")
    telefonoCliente = models.IntegerField(null=False, blank=False, verbose_name="Número Telefónico")
    correoCliente = models.CharField(max_length=100, null=False, blank=False, verbose_name="Correo Electrónico")
    direccionCliente = models.CharField(max_length=150, blank=False, null=False, verbose_name="Dirección")

    def __str__(self):
        return str(self.runCliente)

class TipoEmpleado(models.Model):
    idTipoEmpleado = models.IntegerField(primary_key=True, verbose_name="ID Tipo de Empleado")
    tipoEmpleado = models.CharField(max_length=50 ,null=False, blank=False, verbose_name="Tipo Empleado")

    def __str__(self):
        return self.tipoEmpleado

class PerfilEmpleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idTipoEmpleado = models.ForeignKey(TipoEmpleado, on_delete=models.DO_NOTHING)
    runEmpleado = models.IntegerField(primary_key=True, verbose_name="Run sin puntos")
    dvrunEmpleado = models.CharField(max_length=1, min_lenght=1, blank=False, null=False, verbose_name="-")
    sNombreEmpleado = models.CharField(max_length=50, blank=False, null=False, verbose_name="Segundo Nombre")
    apMaternoEmpleaddo = models.CharField(max_length=50, blank=False, null=False, verbose_name="Apellido Materno")
    fechNacimEmpleado = models.DateField(null=False, blank=False, verbose_name="Fecha de Nacimiento")
    telefonoEmpleado = models.IntegerField(null=False, blank=False, verbose_name="Número Telefónico")
    correoEmpleado = models.CharField(max_length=100, null=False, blank=False, verbose_name="Correo Electrónico")
    direccionEmpleado = models.CharField(max_length=150, blank=False, null=False, verbose_name="Dirección")
    fechaInicCont = models.DateField(null=False, blank=False, verbose_name="Fecha del inicio de Contrato")
    fechaTerCont = models.DateField(null=True, blank=True, verbose_name="Fecha del termino de Contrato")
    sueldoEmp = models.IntegerField(null=False, blank=False, verbose_name="Sueldo de Empleado")

    def __str__(self):
        return str(self.runEmpleado)

class ReservaAtencion(models.Model):
    idCita = models.IntegerField(primary_key=True, verbose_name="Id Cita cliente")
    runCliente = models.ForeignKey(PerfilCliente, on_delete=models.DO_NOTHING)
    precioCita = models.IntegerField(null=False, blank=False, verbose_name="Precio de la Reserva")
    fechaHoraCita = models.DateTimeField(null=False, blank=False, verbose_name="Fecha y Hora de la Cita")
    estadoPago = models.BooleanField(null=False, blank=False, default=False, verbose_name="¿Se ha realizado el pago?")

    def __str__(self):
        return str(self.fechaHoraCita)

class VehiculoCliente(models.Model):
    idVehiculo = models.IntegerField(primary_key=True, verbose_name="Id del Vehiculo")
    runCliente = models.ForeignKey(PerfilCliente, on_delete=models.DO_NOTHING)
    patenteVehiculo = models.CharField(max_length=6, unique=True, null=False, blank=False, verbose_name="Patente del Vehículo")
    marca = models.CharField(max_length=50, null=False, blank=False, verbose_name="Marca del Vehículo")
    modelo = models.CharField(max_length=50, null=False, blank=False, verbose_name="Modelo del Vehículo")
    anio = models.IntegerField(null=False, blank=False, verbose_name="Año del Vehículo")
    
    def __str__(self):
        return self.marca + " " + self.modelo + " De Patente " + self.patenteVehiculo

class Boleta(models.Model):
    idBoleta = models.IntegerField(primary_key=True, verbose_name="# de Boleta")
    idVehiculo = models.ForeignKey(VehiculoCliente, on_delete=models.DO_NOTHING)
    runEmpleado = models.ForeignKey(PerfilEmpleado, on_delete=models.DO_NOTHING)
    fechaBoleta = models.DateField(null=False, blank=False, verbose_name="Fecha de la Boleta")
    precioTotal = models.IntegerField(null=False, blank=False, verbose_name="Precio Total")

    def __str__(self):
        return str(self.idBoleta)

class DetalleBoleta(models.Model):
    idDetalleBoleta = models.IntegerField(primary_key=True, verbose_name="ID del detalle de boleta")
    idBoleta = models.ForeignKey(Boleta, on_delete=models.DO_NOTHING)
    idServicio = models.ForeignKey(Servicio, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.idDetalleBoleta)









