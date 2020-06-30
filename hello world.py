# -*- coding: utf-8 -*-

# PYTHON AVANÇADO: Função reduce #

# Importa a função reduce

from functools import reduce


# Define a função que soma todos os valores da lista

def soma(x, y):
	return x + y

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = reduce(soma, lista)


print(soma)