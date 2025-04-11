from django.contrib import admin
from .models import Apartamento

@admin.register(Apartamento)
class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'andar', 'bloco', 'proprietario')  # Campos a serem exibidos na lista
    search_fields = ('numero', 'bloco', 'proprietario__username')  # Campos para pesquisa
    list_filter = ('andar', 'bloco')  # Filtros na barra lateral