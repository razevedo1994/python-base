#!/usr/bin/env python3
"""Exibe relatorio de criancas por atividades.

Imprimir a lista de criancas agrupadas por sala
que frequenta cada uma das ativadades.
"""
__version__ = "0.1.2"

# Dados
salas = {
    "sala1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"],
}


atividades = {
    "Ingles": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Musica": ["Erik", "Carlos", "Maria"],
    "Danca": ["Gustavo", "Sofia", "Joana", "Antonio"],
}

# Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades.items():

    print(f"Alunos da atividade {nome_atividade}")
    print("-" * 50)

    atividade_sala1 = set(salas["sala1"]) & set(atividade)
    atividade_sala2 = set(salas["sala2"]) & set(atividade)

    print("sala1 ", atividade_sala1)
    print("sala2 ", atividade_sala2)
    print("#" * 50 + "\n")
