from django.db import models

# Cria uma nova classe (modelo) chamada Equipamento que herda de models.Model. 
# Isso diz ao Django que esta classe deve ser mapeada para uma tabela no banco de dados relacional.
 
class Equipamento(models.Model): 
    tombo = models.CharField(max_length=6, unique=True, verbose_name="Tombo") # Cria um campo de texto (CharField) para armazenar o número de tombo do equipamento
    nome_maquina = models.CharField(max_length=100, unique=True, verbose_name="Nome da Máquina") 
    ip_alocado = models.IntegerField(verbose_name="IP Alocado (Final)") # Cria um campo de número inteiro (IntegerField) para armazenar o IP alocado do equipamento
    setor = models.CharField(max_length=50, verbose_name="Setor")

# Verbose_Name: Define um nome amigável para este campo quando ele aparecer em formulários ou no painel administrativo.

    def __str__(self):
        return f"PAT-{self.tombo} - {self.nome_maquina}"


        
# Ele diz ao Python como transformar um objeto da sua classe em uma string (texto legível) quando alguém pedir para imprimi-lo ou convertê-lo em texto.
