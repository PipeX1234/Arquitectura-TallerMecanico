from django.urls import path
from .views import index, why, iniciarSesion, servicio,perfil ,acerca, reservaHora, pagoServicio, webPayPag, gestionarBoleta, gestionarEmpleado, register
from .views import gestionarOrdenesPedido, gestionarProveedores, gestionarServicio, cerrarSesion, PoblarDB, poblarProveedores, gestionarVehiculo, gestionarReserva

urlpatterns = [ 
    path('',index, name="index"),
    path('why', why, name="why"),
    path('register', register, name="register"),
    path('iniciarSesion', iniciarSesion, name="iniciarSesion"),
    path('cerrarSesion',cerrarSesion, name="cerrarSesion"),
    path('servicio', servicio, name="servicio"),
    path('perfil', perfil, name="perfil"),
    path('acerca', acerca, name="acerca"),
    path('reservarHora', reservaHora, name="reservarHora"),
    path('pagoServicio', pagoServicio, name="pagoServicio"),
    path('webpay', webPayPag, name="webpay"),
    path('gestionarBoleta', gestionarBoleta, name="gestionarBoleta"),
    path('gestionarEmpleado', gestionarEmpleado, name="gestionarEmpleado"),
    path('gestionarOrdenesPedido', gestionarOrdenesPedido, name="gestionarOrdenesPedido"),
    path('gestionarProveedores/<action>/<id>', gestionarProveedores, name="gestionarProveedores"),
    path('gestionarVehiculo', gestionarVehiculo, name="gestionarVehiculo"),
    path('gestionarReserva', gestionarReserva, name="gestionarReserva"),
    path('gestionarServicio', gestionarServicio, name="gestionarServicio"),
    path('PoblarDB', PoblarDB, name="PoblarDB"),
    path('poblarProveedores', poblarProveedores, name="poblarProveedores")
]