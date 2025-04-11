from django import forms
from .models import Apartamento

class ApartamentoForm(forms.ModelForm):
    class Meta:
        model = Apartamento
        fields = ['numero', 'andar', 'bloco', 'status', 'proprietario']
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'andar': forms.NumberInput(attrs={'class': 'form-control'}),
            'bloco': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'proprietario': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'numero': 'Número do Apartamento',
            'andar': 'Andar',
            'bloco': 'Bloco/Torre',
            'status': 'Ativo',
            'proprietario': 'Proprietário',
        }
        help_texts = {
            'numero': 'Digite o número do apartamento.',
            'andar': 'Informe o andar do apartamento.',
            'bloco': 'Informe o bloco ou torre do apartamento.',
            'status': 'Marque para indicar que o apartamento está ativo.',
            'proprietario': 'Selecione o proprietário do apartamento.',
        }