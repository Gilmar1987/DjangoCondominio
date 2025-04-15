from django.db import models
from django.forms import ValidationError
from apartamentos.models import Apartamento
from moradores.models import Morador

# Create your models here.
class Visitante(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    data_entrada = models.DateTimeField(auto_now_add=True)
    data_saida = models.DateTimeField(null=True, blank=True)
    autorizado_por = models.ForeignKey(Morador, on_delete=models.CASCADE)
    destino = models.ForeignKey(Apartamento, on_delete=models.CASCADE)
    
    
    

    
    def __str__(self):
        return self.nome
 