# -*- coding: utf-8 -*-

# PYTHON AVANÇADO: Função map #

def dobro(x):
	return x*2

valor = [1, 2, 3, 4, 5]
valor_dobrado = map(dobro, valor)

# Exibe o dobro dos números da lista

for v in valor_dobrado:
	print(v)

# Outra maneira

valor_dobrado = list(valor_dobrado)
print(valor_dobrado)