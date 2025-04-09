from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Proprietario
from .forms import ProprietarioForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ProprietarioListView(ListView):
    model = Proprietario
    template_name = "proprietarios/proprietario_list.html"
    context_object_name = "proprietarios"
    paginate_by = 10

class ProprietarioDetailView(DetailView):
    model = Proprietario
    template_name = "proprietarios/proprietario_detail.html"
    context_object_name = "proprietario"

class ProprietarioCreateView(CreateView):
    model = Proprietario
    form_class = ProprietarioForm
    template_name = "proprietarios/proprietario_form.html"
    success_url = reverse_lazy("proprietario_list")

class ProprietarioUpdateView(UpdateView):
    model = Proprietario
    form_class = ProprietarioForm
    template_name = "proprietarios/proprietario_form.html"
    success_url = reverse_lazy("proprietario_list")

class ProprietarioDeleteView(LoginRequiredMixin,DeleteView):
    model = Proprietario
    template_name = "proprietarios/proprietario_confirm_delete.html"
    success_url = reverse_lazy("proprietario_list")
