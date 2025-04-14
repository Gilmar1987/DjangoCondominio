from django.contrib import admin
from .models import Visitante

from django.utils.translation import gettext_lazy as _
from django.contrib.admin import SimpleListFilter
# Register your models here.
@admin.register(Visitante)
class VisitanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'data_entrada', 'data_saida', 'autorizado_por', 'destino')
    search_fields = ('nome', 'cpf')
    list_filter = ('data_entrada', 'data_saida')
    ordering = ('-data_entrada',)
    
    list_per_page = 10
    list_max_show_all = 100
    list_editable = ('data_saida',)  