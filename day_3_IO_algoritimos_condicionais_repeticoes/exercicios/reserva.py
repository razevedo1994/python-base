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
