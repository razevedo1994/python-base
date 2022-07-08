"""Imprime a mensagem de um e-mail
"""
__version__ = "0.1.1"

import email
import os
import sys

arguments = sys.argv[1:]
if not arguments:
    print("Informe o nome do arquivo de e-mail.")
    sys.exit(1)

filename = arguments[0]
template_name = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
template_path = os.path.join(path, template_name)

for line in open(filepath):
    name, email = line.split(",")

    # TODO: Substituir por envio de email
    print(f"Enviando email para {email}")
    print(
        open(template_path).read()
        % {
            "nome": name,
            "produto": "caneta",
            "texto": "sua ausencia de caneta.",
            "link": "https://caneta.com.br",
            "quantidade": 1,
            "preco": 50,
        }
    )
    print("-" * 50)
