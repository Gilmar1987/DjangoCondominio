from django.db import models
from usuarios.models import Usuario
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Proprietario(Usuario):
    
    telefone = models.CharField(max_length=20)