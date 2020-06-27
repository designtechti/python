# -*- coding: utf-8 -*-

# Python 2 vs Python 3 #

""" 
	1) COMANDO print()
		Em Python 3 passa ser obrigatório o uso de parênteses. Veja:
		- print()

	2) COMANDO input()
		Em Python 2 há duas variações:
		
		# strings
		- raw_input() 

		# valores numéricos
		- input()

		Já em Python 3, deve-se usar apenas input() para strings, e para 
		números  deve-se combinar com as funções int e float. Veja: 
		
		# Recebendo textos
		- meu_texto = input("Digite um texto: ")

		# Recebendo números
		- numero_inteiro = int(input("Digite um número inteiro: "))
		- numero_decimal = float(input("Digite um número decimal: "))
"""