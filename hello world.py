# -*- coding: utf-8 -*-

# Listas (parte 2) #

lista_numerica = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_frutas = ["morango", "abacaxi", "tomate", "limão", "cereja"]

lista_numerica.sort() # Ordena o conteúdo da lista na ordem crescente
print(lista_numerica)

lista_numerica.sort(reverse=True) # Ordena o conteúdo da lista na ordem decrescente
print(lista_numerica)

lista_numerica.reverse() # Reverte o conteúdo da lista
print(lista_numerica)

#	-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-	#

lista_frutas.sort() # Ordena o conteúdo da lista em ordem alfabética
print(lista_frutas)

lista_frutas.sort(reverse=True) # Ordena o conteúdo da lista na ordem decrescente
print(lista_frutas)

lista_frutas.reverse() # Reverte o conteúdo da lista
print(lista_frutas)

#	-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-	#

lista_numerica = sorted(lista_numerica) # Retorna uma lista ordenada
print(lista_numerica)