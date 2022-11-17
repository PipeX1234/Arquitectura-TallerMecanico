from django.urls import path
from .views import index, why, iniciarSesion, servicio, acerca, reservaHora, pagoServicio, webPayPag, gestionarBoleta, gestionarEmpleado
from .views import gestionarOrdenesPedido, gestionarProveedores, gestionarServicio, cerrarSesion, PoblarDB

urlpatterns = [ 
    path('',index, name="index"),
    path('why', why, name="why"),
    path('iniciarSesion', iniciarSesion, name="iniciarSesion"),
    path('cerrarSesion',cerrarSesion, name="cerrarSesion"),
    path('servicio', servicio, name="servicio"),
    path('acerca', acerca, name="acerca"),
    path('reservarHora', reservaHora, name="reservarHora"),
    path('pagoServicio', pagoServicio, name="pagoServicio"),
    path('webpay', webPayPag, name="webpay"),
    path('gestionarBoleta', gestionarBoleta, name="gestionarBoleta"),
    path('gestionarEmpleado', gestionarEmpleado, name="gestionarEmpleado"),
    path('gestionarOrdenesPedido', gestionarOrdenesPedido, name="gestionarOrdenesPedido"),
    path('gestionarProveedores', gestionarProveedores, name="gestionarProveedores"),
    path('gestionarServicio', gestionarServicio, name="gestionarServicio"),
    path('PoblarDB', PoblarDB, name="PoblarDB")
]