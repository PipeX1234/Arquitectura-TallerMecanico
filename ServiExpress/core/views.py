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
#from .models import 
#from .forms import 
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
    return render(request, 'core/login.html')

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
