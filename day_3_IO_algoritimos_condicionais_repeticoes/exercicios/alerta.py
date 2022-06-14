#!/usr/bin/env python3
"""
Alerta de temperatura

Construa um script que pergunta ao usuario qual a temperatura atual e o indice
de umidade do ar. Sera exibida uma mensagem de alerta dependendo
das condicoes:

temp maior 45: ALERTA: Calor extremo
temp vezes 3 for maior ou igual a umidade: ALERTA: Perigo de calor umido
temp entre 10 e 30: Normal
temp entre 0 e 10: Frio
tempo < 0: ALERTA: Frio extremo
"""
import sys

info = {"temperatura": None, "umidade": None}

for key in info.keys():
    try:
        info[key] = float(input(f"Qual a {key}?").strip())
    except ValueError:
        print(f"{key} invalida")
        sys.exit(1)

temperatura = info["temperatura"]
umidade = info["umidade"]

if temperatura > 45:
    print("ALERTA: Perigo de calor extremo")
elif (temperatura * 3) >= umidade:
    print("ALERTA: Perigo de calor umido")
elif temperatura >= 10 and temperatura <= 30:
    print("Temperatura normal")
elif temperatura >= 0 and temperatura <= 10:
    print("Frio")
elif temperatura < 0:
    print("ALERTA: Frio extremo")
