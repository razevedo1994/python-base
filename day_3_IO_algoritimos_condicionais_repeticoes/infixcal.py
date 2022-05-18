#!/usr/bin.env python3
"""Calculadora infix.

Funcionamento:

[operacao] [n1] [n2]

Operacoes:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py 
operacao: sum
n1: 5
n2: 4
9
"""
__version__ = "0.1.0"

import sys

arguments = {"operation": ["sum", "sub", "mul", "div"]}

if sys.argv[1:]:
    operation, n1, n2 = sys.argv[1:]
else:
    operation = input("operacao:")
    n1 = input("n1:")
    n2 = input("n2")

if operation not in arguments["operation"]:
    print(f"Invalid operation {operation}")

if operation == "sum":
    print(int(n1) + int(n2))
elif operation == "sub":
    print(int(n1) - int(n2))
elif operation == "mul":
    print(int(n1) * int(n2))
elif operation == "div":
    print(int(n1) / int(n2))
