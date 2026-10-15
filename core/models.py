from django.db import models

class Equipamento(models.Model):
    SETOR_CHOICES = [
        ('Produção', 'Produção'),
        ('Financeiro', 'Financeiro'),
        ('Engenharia', 'Engenharia'),
        ('TI / Suporte', 'TI / Suporte'),
        ('Recursos Humanos', 'Recursos Humanos'),
        ('Diretoria', 'Diretoria'),
    ]

    tombo = models.CharField(max_length=6, unique=True, verbose_name="Tombo")
    nome_maquina = models.CharField(max_length=100, verbose_name="Nome da Máquina")
    ip_alocado = models.IntegerField(verbose_name="IP Alocado (Final)")
    setor = models.CharField(max_length=50, choices=SETOR_CHOICES, verbose_name="Setor")
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"PAT-{self.tombo} - {self.nome_maquina}"