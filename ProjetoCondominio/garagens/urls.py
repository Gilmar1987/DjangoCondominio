
from django.urls import path
from .views import (
    VagaEstacionamentoListView,
    VagaEstacionamentoDetailView,
    VagaEstacionamentoCreateView,
    VagaEstacionamentoUpdateView,
    VagaEstacionamentoDeleteView,
)



urlpatterns =[
    
    path('garagem/', VagaEstacionamentoListView.as_view(), name='vagaestacionamento_list'),
    path('garagem/<int:pk>/', VagaEstacionamentoDetailView.as_view(), name='vagaestacionamento_detail'),
    path('garagem/create/', VagaEstacionamentoCreateView.as_view(), name='vagaestacionamento_create'),
    path('garagem/update/<int:pk>/', VagaEstacionamentoUpdateView.as_view(), name='vagaestacionamento_update'),
    path('garagem/delete/<int:pk>/', VagaEstacionamentoDeleteView.as_view(), name='vagaestacionamento_delete'),
    
    
]