from django import forms
from django.db.models import Q
from .models import VagaEstacionamento
from apartamentos.models import Apartamento

class VagaEstacionamentoForm(forms.ModelForm):
    info_apartamento = forms.CharField(
        label='Informações do Apartamento',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'})
    )

    class Meta:
        model = VagaEstacionamento
        fields = ['codigo', 'localizacao', 'apartamento', 'info_apartamento']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'localizacao': forms.TextInput(attrs={'class': 'form-control'}),
            'apartamento': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'codigo': 'Código da Vaga',
            'localizacao': 'Localização',
            'apartamento': 'Apartamento',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Define queryset de apartamentos (sem vaga ou o atual se for edição)
        if self.instance and self.instance.pk:
            self.fields['apartamento'].queryset = Apartamento.objects.filter(
                Q(vaga_estacionamento__isnull=True) | Q(pk=self.instance.apartamento.pk)
            )
        else:
            self.fields['apartamento'].queryset = Apartamento.objects.filter(
                vaga_estacionamento__isnull=True
            )
            self.fields.pop('info_apartamento')

        # Formata as opções no select com texto descritivo
        self.fields['apartamento'].label_from_instance = lambda obj: (
            f"Apartamento {obj.numero} - Andar {obj.andar} - Bloco {obj.bloco}"
        )

    def clean(self):
        cleaned_data = super().clean()
        # Remove campo de exibição que não deve ser salvo
        cleaned_data.pop('info_apartamento', None)
        return cleaned_data
