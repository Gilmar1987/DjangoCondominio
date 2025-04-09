
from django.db import models

class ContaCorrente(models.Model):
    id = models.AutoField(primary_key=True)
    numero_conta = models.CharField(max_length=20, unique=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conta {self.numero_conta} - Saldo: {self.saldo}"
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.save()
            return True
        return False
    
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.save()
            return True
        return False
    
    def transferir(self, valor, conta_destino):
        if self.sacar(valor):
            conta_destino.depositar(valor)
            return True
        return False
    
    def get_saldo(self):
        return self.saldo
    
    