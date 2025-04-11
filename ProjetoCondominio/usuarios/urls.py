# usuarios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL para a página inicial
    # Outras URLs específicas para o app usuarios
    # path('perfil/', views.perfil, name='perfil'),
]