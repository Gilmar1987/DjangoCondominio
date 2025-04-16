from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import VagaEstacionamento
from .forms import VagaEstacionamentoForm

# Create your views here.

class VagaEstacionamentoListView(ListView):
    model = VagaEstacionamento
    template_name = 'garagens/vagaestacionamento_list.html'
    context_object_name = 'vagaestacionamentos'
    ordering = ['codigo']  # Ordena por código da vaga de estacionamento    
    
class VagaEstacionamentoDetailView(DetailView):
    model = VagaEstacionamento
    template_name = 'garagens/vagaestacionamento_detail.html'
    context_object_name = 'vagaestacionamento'
    
class VagaEstacionamentoCreateView(CreateView):
    model = VagaEstacionamento
    form_class = VagaEstacionamentoForm
    template_name = 'garagens/vagaestacionamento_form.html'
    success_url = reverse_lazy('vagaestacionamento_list')  # Redireciona para a lista de vagas de estacionamento após criar uma nova vaga
    
class VagaEstacionamentoUpdateView(UpdateView):
    model = VagaEstacionamento
    form_class = VagaEstacionamentoForm
    template_name = 'garagens/vagaestacionamento_form.html'
    success_url = reverse_lazy('vagaestacionamento_list')  # Redireciona para a lista de vagas de estacionamento após atualizar uma vaga
    
class VagaEstacionamentoDeleteView(DeleteView):
    model = VagaEstacionamento
    template_name = 'garagens/vagaestacionamento_confirm_delete.html'
    success_url = reverse_lazy('vagaestacionamento_list')  # Redireciona para a lista de vagas de estacionamento após excluir uma vaga
    
