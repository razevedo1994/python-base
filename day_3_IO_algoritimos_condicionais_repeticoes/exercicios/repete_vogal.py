#!/usr/bin/env python3
"""
Repete vogais

Faca um programa que pede ao usuario que digite uma ou mais palavras e imprime
cada uma das palavras com suas vogais duplicadas.

ex:
python repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Rodrigo
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Roodriigoo
"""


words = []
while True:
    word = input("Digite uma palavra (ou enter para sair):").strip()
    if not word:
        break

    final_word = ""
    for letter in word:
        final_word += letter * 2 if letter.lower() in "aeiou" else letter

    words.append(final_word)

print(*words, sep="\n")
