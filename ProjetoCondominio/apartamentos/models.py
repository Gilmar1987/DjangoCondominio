from django.db import models
from usuarios.models import Usuario
from proprietarios.models import Proprietario

# Create your models here.
class Apartamento(models.Model):
    numero = models.CharField(max_length=10, verbose_name="Número do Apartamento")
    andar = models.IntegerField(blank=True, null=True, verbose_name="Andar")
    bloco = models.CharField(max_length=10, verbose_name="Bloco/Torre")
    status = models.BooleanField(default=True, verbose_name="Status")
    proprietario = models.ForeignKey(Proprietario, on_delete=models.PROTECT, related_name="proprietario_apartamento")
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Apartamento"
        verbose_name_plural = "Apartamentos"
        ordering = ["andar", "numero"]
        constraints = [
        models.UniqueConstraint(fields=['numero', 'bloco'], name='unique_numero_bloco')
    ]

    def __str__(self):
        bloco_str = f" - {self.bloco}" if self.bloco else ""
        andar_str = f" - {self.andar}" if self.andar else ""
        return f"{self.numero}{andar_str}{bloco_str}"
    
    