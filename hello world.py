# -*- coding: utf-8 -*-

# Tratamento de exceções #

a = 2
b = 0

try:
	print(a/b)
except:
	print("Não é possível divisão por 0") 

""" Tenta fazer uma operação matemática 
	e caso não der, emite uma mensagem 
	de erro para poder continuar
	a execução do programa.
"""