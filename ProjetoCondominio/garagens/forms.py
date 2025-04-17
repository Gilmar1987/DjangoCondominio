from django import forms
from django.db.models import Q
from .models import VagaEstacionamento
from apartamentos.models import Apartamento

LOCALIZACOES_BASE = ['Entrada', 'Garagem', 'Área Externa']
VAGAS_POR_LOCALIZACAO = 10

class VagaEstacionamentoForm(forms.ModelForm):
    localizacao = forms.ChoiceField(
        choices=[],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Localização'
    )

    class Meta:
        model = VagaEstacionamento
        fields = ['codigo', 'apartamento', 'localizacao']  # Ordem desejada no formulário

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Ordenação explícita dos campos (opcional, mas garante a ordem)
        self.order_fields(['codigo', 'apartamento', 'localizacao'])

        # Filtra apartamentos sem vaga ou o atual se for edição
        if self.instance and self.instance.pk:
            self.fields['apartamento'].queryset = Apartamento.objects.filter(
                Q(vaga_estacionamento__isnull=True) | Q(pk=self.instance.apartamento.pk)
            )
        else:
            self.fields['apartamento'].queryset = Apartamento.objects.filter(
                vaga_estacionamento__isnull=True
            )

        # Formatação das opções do select apartamento
        self.fields['apartamento'].label_from_instance = lambda obj: (
            f"{obj.numero} | Bloco {obj.bloco}" + (f" | Andar {obj.andar}" if obj.andar else "")
        )

        # Monta as opções de localização apenas se o apartamento já foi selecionado (edição ou POST)
        apartamento = None
        if self.instance and self.instance.pk:
            apartamento = self.instance.apartamento
        elif 'apartamento' in self.data:
            try:
                apartamento_id = int(self.data.get('apartamento'))
                apartamento = Apartamento.objects.get(pk=apartamento_id)
            except (ValueError, Apartamento.DoesNotExist):
                apartamento = None

        if apartamento:
            bloco = apartamento.bloco
            choices = []
            for local in LOCALIZACOES_BASE:
                prefixo = f"{local} - {bloco} - "
                vagas_existentes = VagaEstacionamento.objects.filter(
                    localizacao__startswith=prefixo
                ).values_list('localizacao', flat=True)
                numeros_ocupados = set()
                for vaga in vagas_existentes:
                    partes = vaga.split(' - ')
                    if len(partes) == 3:
                        numeros_ocupados.add(partes[2])
                for i in range(1, VAGAS_POR_LOCALIZACAO + 1):
                    numero_str = f"{i:02d}"
                    if numero_str not in numeros_ocupados:
                        valor = f"{local} - {bloco} - {numero_str}"
                        choices.append((valor, valor))
            if not choices:
                choices = [('', 'Nenhuma vaga disponível para este apartamento/bloco')]
            self.fields['localizacao'].choices = choices
            self.fields['localizacao'].widget.attrs.pop('disabled', None)
        else:
            # Se não tem apartamento selecionado, desabilita o campo e orienta o usuário
            self.fields['localizacao'].choices = [('', 'Selecione um apartamento e salve para escolher a localização')]
            self.fields['localizacao'].widget.attrs['disabled'] = True

    def clean_apartamento(self):
        apartamento = self.cleaned_data['apartamento']
        if self.instance and self.instance.pk:
            if VagaEstacionamento.objects.exclude(pk=self.instance.pk).filter(apartamento=apartamento).exists():
                raise forms.ValidationError("Este apartamento já possui outra vaga vinculada!")
        else:
            if VagaEstacionamento.objects.filter(apartamento=apartamento).exists():
                raise forms.ValidationError("Este apartamento já possui uma vaga vinculada!")
        return apartamento

    def clean(self):
        cleaned_data = super().clean()
        apartamento = cleaned_data.get('apartamento')
        localizacao = cleaned_data.get('localizacao')
        
        #Adicionar Validação forçada
        if apartamento:
            if not localizacao:
                self.add_error('localizacao', 'Este campo é obrigatório.')
            else:
                qs= VagaEstacionamento.objects.filter(localizacao=localizacao)
                if self.instance.pk:
                    qs = qs.exclude(pk=self.instance.pk)
                if qs.exists():
                    raise forms.ValidationError("Esta localização já está ocupada por outra vaga.")
                return cleaned_data
        
         
        if apartamento and localizacao:
            qs = VagaEstacionamento.objects.filter(localizacao=localizacao)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise forms.ValidationError("Esta localização já está ocupada por outra vaga.")
        return cleaned_data
