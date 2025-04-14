from django.contrib import admin
from django.urls import include, path
from .views import VisitanteListView, VisitanteDetailView, VisitanteCreateView, VisitanteUpdateView, VisitanteDeleteView


#app_name = 'visitantes'         

urlpatterns =[
    
    path('', VisitanteListView.as_view(), name='visitante_list'),
    path('visitante/<int:pk>/', VisitanteDetailView.as_view(), name='visitante_detail'),
    path('visitante/create/', VisitanteCreateView.as_view(), name='visitante_create'),
    path('visitante/update/<int:pk>/', VisitanteUpdateView.as_view(), name='visitante_update'), 
    path('visitante/delete/<int:pk>/', VisitanteDeleteView.as_view(), name='visitante_delete'),
]