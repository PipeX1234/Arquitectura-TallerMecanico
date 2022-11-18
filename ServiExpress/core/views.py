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
from .models import PerfilCliente, PerfilEmpleado, Proveedor, TipoEmpleado, SucursalProveedor
from .forms import ProveedorForm, IniciarSesionForm
from datetime import datetime, timedelta, time
import random
#import requests
import json
# Create your views here.
    # elif not (request.user.is_authenticated and request.user.is_staff):
    #     return redirect(index)

def index(request):
    return render(request, 'core/index.html')

def why(request):
    if request.user.is_superuser:
        return redirect(index)
    return render(request, 'core/why.html')

def iniciarSesion(request):
    if request.user.is_authenticated:
        return redirect(index)
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
    if not request.user.is_authenticated:
        return redirect(index)

    logout(request)
    return redirect(index)

def servicio(request):
    return render(request, 'core/service.html')

def acerca(request):
    if request.user.is_superuser:
        return redirect(index)

    return render(request, 'core/about.html')

def reservaHora(request):
    if not request.user.is_authenticated:
        return redirect(index)
    return render(request, 'core/reservaHoraCli.html')

def pagoServicio(request):
    if not request.user.is_authenticated:
        return redirect(index)
    return render(request, 'core/payment.html')

def webPayPag(request):
    if not request.user.is_authenticated:
        return redirect(index)
    return render(request, 'core/webpay.html')

def gestionarBoleta(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect(index)
    return render(request,'core/gestionarBoleta.html')

def gestionarEmpleado(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect(index)
    return render(request, 'core/gestionarEmpleado.html')

def gestionarOrdenesPedido(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect(index)
    return render(request, 'core/gestionarOrdenesPedido.html')

def gestionarProveedores(request, action, id):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect(index)

    data = {"mesg":"", "form":ProveedorForm, "action":action, "id":id}

    if(action == 'ins'):

        if request.method == "POST":
            form = ProveedorForm(request.POST)
            if form.is_valid:
                print("Es valido")
                try:
                    form.save()
                    data["mesg"] = "El Proveedor se ha agregado correctamente"
                    data["action"] = "na"
                except:
                    data["mesg"] = "No se ha logrado agregar el proveedor, revise los datos o intentelo de nuevo más tarde"

    elif(action == 'upd'):

        objeto = Proveedor.objects.get(idProveedor=id)
        if request.method == "POST":
            form = ProveedorForm(data=request.POST, instance=objeto)
            if form.is_valid:
                print("Es valido")
                try:
                    form.save()
                    data["mesg"] = "Se han actualizado los datos del proveedor correctamente"
                    data["action"] = "na"
                except Exception as err:
                    print(f"ha ocurrido un error al editar {err}")
                    data["mesg"] = "No se ha logrado actualizar al proveedor, revise los datos o intentelo más tarde"

        data["form"] = ProveedorForm(instance=objeto)
        

    elif(action == 'del'):

        try:
            Proveedor.objects.get(idProveedor=id).delete()
            data["mesg"] = "Se ha eliminado el proveedor correctamente"
            return redirect(gestionarProveedores, action='na', id = '-1')
        except:
            data["mesg"] = "No se ha podido eliminar, actualice la página y revise si existe o intentelo nuevamente más tarde"
        
    else:
        print("Solo se está listando")

    data["list"] = Proveedor.objects.all().order_by('idProveedor').values('idProveedor','idSucursalProveedor__region', 
        'idSucursalProveedor__comuna', 'nombreProveedor', 'correoProveedor', 'telefonoProveedor')
    return render(request, 'core/gestionarProveedores.html', data)

def gestionarServicio(request):
    if not request.user.is_authenticated:
        return redirect(index)
    return render(request, 'core/gestionarServicios.html')

def poblarProveedores(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect(index)

    try:
        #Se eliminan los proveedores
        try:
            print("Intentando Eliminar Proveedores")
            SucursalProveedor.objects.all().delete()
            Proveedor.objects.all().delete()
        except Exception as err:
            print(f"Error al intentar eliminar proveedores: {err}")
        
        #Se intentan crear las sucursales del proveedor
        try:
            print("Creando Sucursales Proveedor")
            SucursalProveedor.objects.create(idSucursalProveedor=1, region="Santiago", comuna="Recoleta")
            SucursalProveedor.objects.create(idSucursalProveedor=2, region="Santiago", comuna="Las Condes")
            SucursalProveedor.objects.create(idSucursalProveedor=3, region="Valparaíso", comuna="Valparaíso")
            SucursalProveedor.objects.create(idSucursalProveedor=4, region="Arica", comuna="Arica")
        except Exception as err:
            print(f"Error al crear las sucursales proveedor: {err}")

        try:
            print("Intentando crear los Proveedores")
            Proveedor.objects.create(idProveedor=1, idSucursalProveedor=SucursalProveedor.objects.get(idSucursalProveedor=1), 
                nombreProveedor="Chevrolet", correoProveedor="proveedor@chevrolet.com", telefonoProveedor=48751684)
            Proveedor.objects.create(idProveedor=2, idSucursalProveedor=SucursalProveedor.objects.get(idSucursalProveedor=2), 
                nombreProveedor="Toyota", correoProveedor="proveedor@toyota.com", telefonoProveedor=48751684)
            Proveedor.objects.create(idProveedor=3, idSucursalProveedor=SucursalProveedor.objects.get(idSucursalProveedor=4), 
                nombreProveedor="Suzuli", correoProveedor="proveedor@suzuki.com", telefonoProveedor=48751684)
        except Exception as err:
            print(f"Error al intentar crear los proveedores: {err}")

    except Exception as err:
        print(f"Error en el proceso de Poblar Proveedores: {err}")

    return redirect(gestionarProveedores)


def PoblarDB(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect(index)
    
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
