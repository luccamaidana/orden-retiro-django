# core/urls.py

from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('ordenes/nueva/', views.crear_orden_retiro, name='crear_orden_retiro'),
]