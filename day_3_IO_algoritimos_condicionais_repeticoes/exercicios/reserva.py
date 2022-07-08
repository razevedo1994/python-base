#!/usr/bin/env python3
"""
Faca um programa de terminal que exibe ao usuario uma lista dos quartos
disponiveis para alugar e o preco de cadas quarto, esta informacao esta
disponivel em um arquivo de texte separado por virgulas.

`quartos.txt`
codigo,nome,preco
1,Suite Master,500
2,Quarto Familia,200
2,Quarto Single,100
4,Quarto Simples,50

O programa pergunta ao usuario o nome, qual o numero do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago.

O programa deve salvar esta escolha em um outro arquivo contendo as reservas.

`reservas.txt`
cliente,quarto,dias
Rodrigo,3,12


Se outro usuario tentar reservar o mesmo quarto o programa deve exibir uma
mensagem informando que ja esta reservado.
"""
import sys
import logging


ocupados = {}
try:
    for line in open("reservas.txt"):
        nome, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome": nome,
            "dias": dias,
        }
except FileNotFoundError:
    logging.error("Arquivo reservas.txt nao existe")
    sys.exit(1)


quartos = {}
try:
    for line in open("quartos.txt"):
        codigo, nome, preco = line.strip().split(",")
        quartos[int(codigo)] = {
            "nome": nome,
            "preco": float(preco),  # TODO: Decimal
            "disponivel": False if int(codigo) in ocupados else True,
        }
except FileNotFoundError:
    logging.error("Arquivo quartos.txt nao existe")
    sys.exit(1)


print("\nReserva Hotel Pythonico\n")
print("-" * 30)
nome_cliente = input("\nNome do cliente: ").strip()


if len(ocupados) == len(quartos):
    print("Hotel Lotado.")


print("Lista de quartos:\n")
for codigo, dados in quartos.items():
    nome = dados["nome"]
    preco = dados["preco"]
    disponivel = "🚫" if not dados["disponivel"] else "✅"
    # TODO: Substituir casa decimal por virgula
    print(f"{codigo} - {nome} - R$ {preco:.2f} - {disponivel}")

print("-" * 30)
try:
    num_quarto = int(input("Numero do quarto: ").strip())
    if not quartos[num_quarto]["disponivel"]:
        print(f"O quarto {num_quarto} esta ocupado")
        sys.exit(1)
except ValueError:
    logging.error("Numero invalido, digite apenas digitos.")
    sys.exit(1)
except KeyError:
    print(f"O quarto {num_quarto} nao existe.")
    sys.exit(1)

try:
    dias = int(input("Quantidade de dias: ").strip())
except ValueError:
    logging.error("Numero invalido, digite apenas digitos.")
    sys.exit(1)

nome_quarto = quartos[num_quarto]["nome"]
preco_quarto = quartos[num_quarto]["preco"]
disponivel = quartos[num_quarto]["disponivel"]

total = preco_quarto * dias

with open("reservas.txt", "a") as file_:
    file_.write(f"{nome_cliente},{num_quarto},{dias}\n")

print(
    f"{nome_cliente} voce escolheu o quarto {nome_quarto} e vai custar: R${total:.2f}"
)
