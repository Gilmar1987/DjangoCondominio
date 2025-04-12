from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import MoradorListView, MoradorDetailView, MoradorCreateView, MoradorUpdateView, MoradorDeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

urlpatterns = [
   # path('admin/', admin.site.urls),
    
    path('',MoradorListView.as_view(), name='morador_list'),    
    path('morador/<int:pk>/', MoradorDetailView.as_view(), name='morador_detail'),   
    path('morador/create/', MoradorCreateView.as_view(), name='morador_create'), 
    path('morador/update/<int:pk>/', MoradorUpdateView.as_view(), name='morador_update'),    
    path('morador/delete/<int:pk>/', MoradorDeleteView.as_view(), name='morador_delete'),    
     
   
]
