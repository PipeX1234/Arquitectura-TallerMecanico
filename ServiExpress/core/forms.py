from dataclasses import field
from msilib.schema import CheckBox
from pyexpat import model
from django import forms
from django.forms import ModelForm, fields, Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from pkg_resources import require
from .models import SucursalProveedor, Proveedor, EstadoOrden, Producto, OrdenDePedido, DetalleOrden, TipoServicio, Servicio, PerfilCliente 
from .models import TipoEmpleado, PerfilEmpleado, ReservaAtencion, VehiculoCliente, Boleta, DetalleBoleta
# from .models

class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['idSucursalProveedor', 'nombreProveedor', 'correoProveedor', 'telefonoProveedor']

class IniciarSesionForm(Form):
    username = forms.CharField(widget=forms.TextInput(), label="Correo")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    class Meta:
        fields = ['username', 'password']

# class RegistrarUsuarioForm(UserCreationForm):
#     rutUsuario = forms.CharField(max_length=12, required=True, label="Rut")
#     direccion = forms.CharField(max_length=300, required=True, label="Direccion")
#     esSuscriptor = forms.BooleanField(required=False,label="Tener suscripción")
#     imagen = forms.ImageField(required=False, label="Imagen de Usuario")
#     class Meta:
#         model = User
#         fields = ['username', 'first_name','last_name', 'email', 'imagen','rutUsuario', 'direccion','esSuscriptor']

# class EditarUsuario(Form):
#     first_name = forms.CharField(max_length=150,required=True,label="Nombres")
#     last_name = forms.CharField(max_length=150, required=True, label="Apellidos")
#     email = forms.CharField(max_length=254, required=True, label="Correo")
#     rutUsuario = forms.CharField(max_length=12, required=True, label="Rut")
#     direccion = forms.CharField(max_length=300, required=True, label="Direccion")
#     esSuscriptor = forms.BooleanField(required=False,label="Tener suscripción")
#     imagen = forms.ImageField(label="Imagen Usuario", required=False)
#     class Meta:
#         fields = '__all__'