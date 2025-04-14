from django import forms
from .models import Visitante

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = ['nome', 'documento', 'telefone', 'email', 'data_entrada', 'data_saida', 'autorizado_por', 'destino']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'data_entrada': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'data_saida': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'autorizado_por': forms.Select(attrs={'class': 'form-control'}),
            'destino': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome do Visitante',
            'documento': 'Documento de Identidade',
            'telefone': 'Telefone',
            'email': 'E-mail',
            'data_entrada': 'Data de Entrada',
            'data_saida': 'Data de Saída',
            'autorizado_por': 'Autorizado por',
            'destino': 'Destino',
        }
        help_texts = {
            'nome': 'Digite o nome completo do visitante.',
            'documento': 'Informe o número do documento de identidade.',
            'telefone': 'Informe o telefone para contato.',
            'email': 'Informe um e-mail válido.',
            'data_entrada': 'Selecione a data e hora de entrada.',
            'data_saida': 'Selecione a data e hora de saída.',
            'autorizado_por': 'Selecione o morador que autorizou a entrada.',
            'destino': 'Selecione o apartamento de destino.',
        }