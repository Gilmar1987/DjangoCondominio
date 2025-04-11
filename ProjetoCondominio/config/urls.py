
from django import views
from django.contrib import admin
from django.urls import include, path
from usuarios import views as usuarios_views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('usuarios.urls')),  # URL para a página inicial
    path('proprietarios/', include('proprietarios.urls')),
    path('apartamentos/', include('apartamentos.urls')),
    path('moradores/', include('moradores.urls')),
    
    
    
   
]