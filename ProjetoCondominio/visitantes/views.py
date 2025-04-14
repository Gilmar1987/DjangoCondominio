from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Visitante
from .forms import VisitanteForm    

class VisitanteListView(ListView):
    model = Visitante
    template_name = 'visitantes/visitante_list.html'
    context_object_name = 'visitantes'
    ordering = ['nome'] # Ordena por nome
    
class VisitanteDetailView(DetailView):
    model = Visitante
    template_name = 'visitantes/visitante_detail.html'
    context_object_name = 'visitante'
    
class VisitanteCreateView(CreateView):
    model = Visitante
    form_class = VisitanteForm
    template_name = 'visitantes/visitante_form.html'
    success_url = reverse_lazy('visitante_list') # Redireciona para a lista de visitantes após criar um novo visitante   
    
class VisitanteUpdateView(UpdateView):
    model = Visitante
    form_class = VisitanteForm
    template_name = 'visitantes/visitante_form.html'
    success_url = reverse_lazy('visitante_list') # Redireciona para a lista de visitantes após atualizar um visitante
    
class VisitanteDeleteView(DeleteView):
    model = Visitante
    template_name = 'visitantes/visitante_confirm_delete.html'
    success_url = reverse_lazy('visitante_list') # Redireciona para a lista de visitantes após excluir um visitante  
    
    
    

# Create your views here.
