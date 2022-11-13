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
import requests
import json
# Create your views here.
