from django.db import models
from apartamentos.models import Apartamento
 # Create your models here.
 
 
class VagaEstacionamento(models.Model):
    codigo = models.CharField(max_length=10)
    apartamento = models.OneToOneField(Apartamento, on_delete=models.CASCADE, related_name='vaga_estacionamento')
    localizacao = models.CharField(max_length=50)
        
    def __str__(self):
        return f"Vaga {self.codigo} - Apartamento {self.apartamento.numero}"