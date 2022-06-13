#!/usr/bin/env python3
"""
Construa um programa que imprime os numeros pares de 1 a 200

ex
`python numeros_pares.py`

>> 2
>> 4
>> 6
>> 8
...
"""
for numero in range(1, 201):
    if numero % 2 == 0:
        print(numero)
