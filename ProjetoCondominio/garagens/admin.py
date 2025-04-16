from django.contrib import admin
from .models import VagaEstacionamento

@admin.register(VagaEstacionamento)
class VagaEstacionamentoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'localizacao', 'apartamento', 'info_apartamento')  # Adiciona 'info_apartamento' ao list_display
    search_fields = ('codigo', 'localizacao', 'apartamento__numero')
    readonly_fields = ('info_apartamento',)  # Adiciona 'info_apartamento' como readonly

    def info_apartamento(self, obj):
        """
        Exibe informações sobre o bloco, andar e número do apartamento.
        """
        return f"Bloco: {obj.apartamento.bloco}, Andar: {obj.apartamento.andar}, Número: {obj.apartamento.numero}"

    info_apartamento.short_description = "Informações do Apartamento"  # Define o cabeçalho da coluna