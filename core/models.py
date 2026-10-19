from django.db import models

class Equipamento(models.Model):
    tombo = models.CharField(max_length=6, unique=True, verbose_name="Tombo")
    nome_maquina = models.CharField(max_length=100, unique=True, verbose_name="Nome da Máquina")
    ip_alocado = models.IntegerField(verbose_name="IP Alocado (Final)")
    setor = models.CharField(max_length=50, verbose_name="Setor")


    def __str__(self):
        return f"PAT-{self.tombo} - {self.nome_maquina}"