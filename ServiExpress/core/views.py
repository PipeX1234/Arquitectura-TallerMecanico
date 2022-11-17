from django.shortcuts import redirect, render
from ast import Pass
from asyncio.windows_events import NULL
from tkinter.tix import Form
from tokenize import Double
from django.views.decorators.csrf import csrf_exempt
from logging import exception
from rest_framework.authentication import RemoteUserAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth import login, logout, authenticate
from .models import PerfilCliente, PerfilEmpleado, Proveedor, TipoEmpleado
from .forms import ProveedorForm, IniciarSesionForm
from datetime import datetime, timedelta, time
import random
#import requests
import json
# Create your views here.


def index(request):
    return render(request, 'core/index.html')

def why(request):
    return render(request, 'core/why.html')

def iniciarSesion(request):
    data = {"mesg": "", "form": IniciarSesionForm}

    if request.method == "POST":
        form = IniciarSesionForm(request.POST)
        if form.is_valid:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(index)
                else:
                    data["mesg"] = "¡La cuenta o la password no son correctos!"
            else:
                data["mesg"] = "¡La cuenta o la password no son correctos!"
    return render(request, 'core/login.html', data)

def cerrarSesion(request):
    logout(request)
    return redirect(index)

def servicio(request):
    return render(request, 'core/service.html')

def acerca(request) :
    return render(request, 'core/about.html')

def reservaHora(request):
    return render(request, 'core/reservaHoraCli.html')

def pagoServicio(request):
    return render(request, 'core/payment.html')

def webPayPag(request):
    return render(request, 'core/webpay.html')

def gestionarBoleta(request):
    return render(request,'core/gestionarBoleta.html')

def gestionarEmpleado(request):
    return render(request, 'core/gestionarEmpleado.html')

def gestionarOrdenesPedido(request):
    return render(request, 'core/gestionarOrdenesPedido.html')

def gestionarProveedores(request):
    return render(request, 'core/gestionarProveedores.html')

def gestionarServicio(request):
    return render(request, 'core/gestionarServicios.html')


def PoblarDB(request):
    ##Se crean los tipo empleado
    try:
        print("Se intentan crear los tipos Empleados")
        TipoEmpleado.objects.create(idTipoEmpleado=1 ,tipoEmpleado="Administrador")
        TipoEmpleado.objects.create(idTipoEmpleado=2 ,tipoEmpleado="Secretario")
        TipoEmpleado.objects.create(idTipoEmpleado=3 ,tipoEmpleado="Mecanico")
        print("Se han creado los distintos tipos de empleados")
    except Exception as err:
        print(f"error al crear los tipos de empleado: {err}")
    ##Se crea un usuario Admin
    try:
        print("Verificar si existe usuario Admin.")
        if User.objects.filter(username="JuanM").exists():
            print("Intentando eliminar usuario Admin.")
            User.objects.get(username="JuanM").delete()
            print("Usuario Admin eliminado.")
        print("Iniciando creación de usuario cliente.")
        user = User.objects.create_user(username="JuanM", password='Juan#123')
        user.first_name = "Juan"
        user.last_name = "Martinez"
        user.email = "JuanM@ServiExpress.com"
        user.is_superuser = True
        user.is_staff = True
        PerfilEmpleado.objects.create(user=user, idTipoEmpleado=TipoEmpleado.objects.get(idTipoEmpleado = 1), runEmpleado=15466788,
            dvrunEmpleado="k", sNombreEmpleado="Pedro", apMaternoEmpleaddo="Perez", fechNacimEmpleado="1993-10-19", telefonoEmpleado=78526413,
            correoEmpleado="JuanM@ServiExpress.com", direccionEmpleado="Las Condes 123", fechaInicCont="2021-11-15", sueldoEmp=650000)
        user.save()
        print("Usuario Admin fue creado correctamente.")
    except Exception as err:
        print(f"Error al crear usuario Admin: {err}")
    ##Se intenta crear un usuario Empleado Secretario
    try:
        print("Verificar si existe usuario Secretario.")
        if User.objects.filter(username="LucasSec").exists():
            print("Intentando eliminar usuario Secretario.")
            User.objects.get(username="LucasSec").delete()
            print("Usuario Secretario eliminado.")
        print("Iniciando creación de usuario Secretario.")
        user = User.objects.create_user(username="LucasSec", password='Lucas#123')
        user.first_name = "Lucas"
        user.last_name = "Collao"
        user.email = "LucasSec@ServiExpress.com"
        user.is_superuser = False
        user.is_staff = True
        PerfilEmpleado.objects.create(user=user, idTipoEmpleado=TipoEmpleado.objects.get(idTipoEmpleado=2), runEmpleado=11556789,
            dvrunEmpleado="3", sNombreEmpleado="Ivan", apMaternoEmpleaddo="García", fechNacimEmpleado="1988-01-15", telefonoEmpleado=45781264,
            correoEmpleado="LucasSec@ServiExpress.com", direccionEmpleado="Calle Lampa 7889", fechaInicCont="2022-03-25", sueldoEmp=450000)
        user.save()
        print("Usuario Secretario fue creado correctamente.")
    except Exception as err:
        print(f"Error al crear usuario Secretario: {err}")
    ##Se intenta crear usuario Cliente
    try:
        print("Verificar si existe usuario Cliente.")
        if User.objects.filter(username="MartinCli").exists():
            print("Intentando eliminar usuario Cliente.")
            User.objects.get(username="MartinCli").delete()
            print("Usuario Cliente eliminado.")
        print("Iniciando creación de usuario Cliente.")
        user = User.objects.create_user(username="MartinCli", password='Martin#123')
        user.first_name = "Martin"
        user.last_name = "López"
        user.email = "MartinLopez@gmail.com"
        user.is_superuser = False
        user.is_staff = False
        PerfilCliente.objects.create(user=user, runCliente=15460778, dvrunCliente="1", sNombreCliente="Alejandro", apMaternoCliente="Sánchez",
            fechNacimCliente="2000-04-02", telefonoCliente=78541597, correoCliente="MartinLopez@gmail.com", direccionCliente="Las Enredaderas 2324")
        user.save()
        print("Usuario Cliente fue creado correctamente.")
    except Exception as err:
        print(f"Error al crear usuario Secretario: {err}")
    return redirect(index)
