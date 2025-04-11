from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Morador
from .forms import MoradorForm
from django.contrib.auth.mixins import LoginRequiredMixin


class MoradorListView(ListView):
    model = Morador
    template_name = "moradores/morador_list.html"
    context_object_name = "morador"
    paginate_by = 10

class MoradorDetailView(DetailView):
    model = Morador
    template_name = "moradores/morador_detail.html"
    context_object_name = "morador"

class MoradorCreateView(CreateView):
    model = Morador
    form_class = MoradorForm
    template_name = "moradores/morador_form.html"
    success_url = reverse_lazy("morador_list")

class MoradorUpdateView(UpdateView):
    model = Morador
    form_class = MoradorForm
    template_name = "moradores/morador_form.html"
    success_url = reverse_lazy("morador_list")

class MoradorDeleteView(LoginRequiredMixin,DeleteView):
    model = Morador
    template_name = "moradores/morador_confirm_delete.html"
    success_url = reverse_lazy("morador_list")
