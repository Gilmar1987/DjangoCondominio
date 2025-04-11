from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Apartamento
from .forms import ApartamentoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
class ApartamentoListView(ListView):
    model = Apartamento
    template_name = 'apartamentos/apartamento_list.html'
    context_object_name = 'apartamentos'
    paginate_by = 10    

class ApartamentoDetailView(DetailView):
    model = Apartamento
    template_name = 'apartamentos/apartamento_detail.html'
    context_object_name = 'apartamento' 
    
class ApartamentoCreateView(CreateView):
    model = Apartamento
    form_class = ApartamentoForm
    template_name = 'apartamentos/apartamento_form.html'
    success_url = reverse_lazy('apartamento_list')
    
class ApartamentoUpdateView(UpdateView):
    model = Apartamento
    form_class = ApartamentoForm
    template_name = 'apartamentos/apartamento_form.html'
    success_url = reverse_lazy('apartamento_list')
    
class ApartamentoDeleteView(LoginRequiredMixin, DeleteView):
    model = Apartamento
    template_name = 'apartamentos/apartamento_confirm_delete.html'
    success_url = reverse_lazy('apartamento_list')
    