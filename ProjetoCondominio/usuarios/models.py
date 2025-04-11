from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    PERFIS = (
        ('sindico', 'Síndico'),
        ('porteiro', 'Porteiro'),
        ('morador', 'Morador'),
        ('proprietario', 'Proprietário'),
    )
    perfil = models.CharField(max_length=20, choices=PERFIS)
    
    def __str__(self):
        return self.username


