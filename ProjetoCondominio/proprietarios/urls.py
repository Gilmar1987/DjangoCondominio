from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import (
    ProprietarioListView, 
    ProprietarioDetailView,
    ProprietarioCreateView, 
    ProprietarioUpdateView, 
    ProprietarioDeleteView
)

urlpatterns = [
   # path('admin/', admin.site.urls),
    
    path('',ProprietarioListView.as_view(), name='proprietario_list'),    
    path('proprietario/<int:pk>/', ProprietarioDetailView.as_view(), name='proprietario_detail'),   
    path('proprietario/create/', ProprietarioCreateView.as_view(), name='proprietario_create'), 
    path('proprietario/update/<int:pk>/', ProprietarioUpdateView.as_view(), name='proprietario_update'),    
    path('proprietario/delete/<int:pk>/', ProprietarioDeleteView.as_view(), name='proprietario_delete'),    
     
   
]
