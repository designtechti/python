# -*- coding: utf-8 -*-

# PYTHON AVANÇADO: Função enumerate #

lista = ["abacate", "bola", "cachorro"]

# Exibe o número do índice de uma lista da forma mais simples

for i in range(len(lista)):
	print(i, lista[i])

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

# Exibe o número do índice de uma lista com a função enumerate

for i, nome in enumerate(lista):
	print(i, nome)
