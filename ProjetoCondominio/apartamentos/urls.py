
from django.contrib import admin
from django.urls import include, path
from .views import (ApartamentoListView, 
                    ApartamentoDetailView, 
                    ApartamentoCreateView, 
                    ApartamentoUpdateView, 
                    ApartamentoDeleteView ) 

urlpatterns = [ 
               
    path('',ApartamentoListView.as_view(), name='apartamento_list'),    
    path('apartamento/<int:pk>/', ApartamentoDetailView.as_view(), name='apartamento_detail'),   
    path('apartamento/create/', ApartamentoCreateView.as_view(), name='apartamento_create'), 
    path('apartamento/update/<int:pk>/', ApartamentoUpdateView.as_view(), name='apartamento_update'),    
    path('apartamento/delete/<int:pk>/', ApartamentoDeleteView.as_view(), name='apartamento_delete'),   
               
 ]