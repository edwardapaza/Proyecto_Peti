from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('mision', views.mision, name='mision'),
    path('vision', views.vision, name='vision'),
    path('valores', views.valores, name='valores'),
]
