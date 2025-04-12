from django import forms
from .models import Morador
from usuarios.models import Usuario  # Importe o model Usuario

class MoradorForm(forms.ModelForm):
    """
    Formulário para criar ou atualizar um Morador.
    """
    class Meta:
        model = Morador
        fields = ['username','first_name', 'last_name',  'email', 'perfil', 'password', 'apartamento', 'telefone', 'data_nascimento']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'perfil': forms.Select(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'apartamento': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'username': 'Nome de Usuário',
            'email': 'Email',
            'perfil': 'Perfil',
            'password': 'Senha',
            'telefone': 'Telefone',
            'data_nascimento': 'Data de Nascimento',
            'apartamento': 'Apartamento',
        }
        help_texts = {
            'username': 'O nome de usuário deve ser único.',
            'email': 'Informe um endereço de email válido.',
            'password': 'A senha deve ter pelo menos 8 caracteres.',
            'perfil': 'Selecione o perfil do morador.',
            'telefone': 'Informe o número de telefone do morador.',
            'data_nascimento': 'Informe a data de nascimento do morador.',
            'apartamento': 'Selecione o apartamento do morador.',
        }

    def save(self, commit=True):
        """
        Sobrescreve o método save para lidar com a criação do usuário e do perfil de morador.
        """
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        user.set_password(password)  # Encripta a senha
        if commit:
            user.save()
        return user