# -*- coding: utf-8 -*-

# PYTHON AVANÇADO: Função zip #

"""
	Esta função concatena os valores 
	de cada lista e exibe na tela 
	tudo junto.
"""

lista_numerica = [1, 2, 3, 4, 5]
lista_string = ["abacaxi", "banana", "carambola", "dedo-de-moça", "estrela-do-mar"]
lista_valor = ["R$ 1,00", "R$ 2,00", "R$ 3,00", "R$ 4,00", "R$ 5,00"]

for numero, nome, valor in zip(lista_numerica, lista_string, lista_valor):
	print(numero, nome, valor)