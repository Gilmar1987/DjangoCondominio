from email.headerregistry import Group
from django.db import models
from usuarios.models import Usuario
from django.contrib.auth.models import Permission

# Create your models here.
class Proprietario(Usuario):
    
    telefone = models.CharField(max_length=20)

   
    class Meta:
            
            verbose_name = "Proprietário"
            verbose_name_plural = "Proprietários"
            ordering = ["username"]
            
            def __str__(self):
                return self.username