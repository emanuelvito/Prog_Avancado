from core.models import Ramal

RAMAIS = [
    ("2004", "Pedro Silva", "SESMT", "Seguranca do Trabalho"),
    ("2001", "João Silva", "PRODUCAO", "PRODUCAO"),
    ("2005", "Maria Santos", "TI", "Suporte Local"),
    ("2012", "Carlos Eduardo", "LOGISTICA", "Galpão B"),
    ("2022", "Ana Silva", "LABORATORIO", "Galpão A"),
    ("2024", "Joao Maria", "FROTA", "FROTA"),
    ("2026", "Rafael Santos", "ALMOXARIFADO", "ALMOXARIFADO"),
    ("2028", "Carlos Eduardo", "MANUTENCAO", "MANUTENCAO"),
    ("2030", "Maria Madalena", "PRODUCAO", "PRODUCAO"),
    ("2031", "Thiago Silva", "MANUTENCAO", "MANUTENCAO") 
]
for numero, colaborador, setor, observacao in RAMAIS:
    ramal, criado = Ramal.objects.update_or_create(
        numero=numero,
        defaults={
            "colaborador": colaborador,
            "setor": setor,
            "observacao": observacao,
        },
    )
    print(("Criado:    " if criado else "Atualizado:"), ramal)

print(f"Total de ramais no banco: {Ramal.objects.count()}")