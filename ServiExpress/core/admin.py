from django.contrib import admin
from .models import SucursalProveedor, Proveedor, EstadoOrden, Producto, OrdenDePedido, DetalleOrden, TipoServicio, Servicio, PerfilCliente 
from .models import TipoEmpleado, PerfilEmpleado, ReservaAtencion, VehiculoCliente, Boleta, DetalleBoleta
# Register your models here.

admin.site.register(SucursalProveedor)
admin.site.register(Proveedor)
admin.site.register(EstadoOrden)
admin.site.register(Producto)
admin.site.register(OrdenDePedido)
admin.site.register(DetalleOrden)
admin.site.register(TipoServicio)
admin.site.register(Servicio)
admin.site.register(PerfilCliente)
admin.site.register(TipoEmpleado)
admin.site.register(PerfilEmpleado)
admin.site.register(ReservaAtencion)
admin.site.register(VehiculoCliente)
admin.site.register(Boleta)
admin.site.register(DetalleBoleta)
