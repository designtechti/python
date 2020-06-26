# -*- coding: utf-8 -*-

# Dicionários #

"""
	Em python, Dicionários são arrays associativos, 
	ou seja, um determinado valor passa 
	a ser vinculado à uma chave. 
"""

redes_sociais = {"Design_Tech_TI" : "@designtechti"} # Dicionários em Pyhon

""" 
	No dicionário acima, 
	a chave "Design Tech TI" 
	foi vinculado 
	ao valor "@designtechti".
	Para imprimí-los, basta seguir 
	o comando abaixo: 
"""

print(redes_sociais['Design_Tech_TI']) # Exibe na tela as redes sociais de Design Tech TI

"""
	Se o dicionário tiver vários elementos, 
	pode-se usar laços de repetição
	para imprimí-los: 
"""

redes_sociais = {"Design_Tech_TI" : "@designtechti", "Google" : "@google", "Udemy" : "@udemy"} # Dicionários em Pyhon

for chave in redes_sociais: # Imprime todos os itens do dicionário redes_sociais
	print(redes_sociais[chave])