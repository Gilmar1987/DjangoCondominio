from django.db import models
from usuarios.models import Usuario
from apartamentos.models import Apartamento
from proprietarios.models import Proprietario
from django.contrib.auth.models import Permission
from django.contrib.auth.models import AbstractUser, Permission

# Create your models here.
class Morador(Usuario):
    #usuario = models.OneToOneField(Proprietario, on_delete=models.CASCADE, related_name="morador_usuario")
    apartamento = models.ForeignKey(Apartamento, on_delete=models.PROTECT, related_name="morador_apartamento")
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        
        verbose_name = "Morador"
        verbose_name_plural = "Moradores"
        
        def __str__(self):
            return self.username