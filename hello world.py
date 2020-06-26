# -*- coding: utf-8 -*-

# Listas (parte 1) #

lista_string = ["abacaxi", "melancia", "abacate"]
lista_numerica = [1,2,3,4,5]
lista_aleatoria = ["abacate", 2, True, 9.89]
tamanho = len(lista_aleatoria)

print(lista_string)
print(lista_numerica)
print(lista_aleatoria)

print(lista_numerica[3]) # Exibe na tela o 3º item da lista, começando desde o 0.

for item in lista_string: # Exibe na tela os itens da lista item por item.
	print (item)

print(tamanho) # Exibe quantos itens tem dentro da lista.

lista_string.append("limão")
print(lista_string)

if 9.99 in lista_aleatoria: # Faz uma busca de um item da lista.
	print("9.99 está na lista")
else:
	print("9.99 não está na lista")	

del lista_numerica[1:3] # Remove itens da lista desde o 1º até o item 3.
print(lista_numerica)

del lista_numerica[:] # Apaga todos os itens da lista
print(lista_numerica)

nova_lista = []

nova_lista.append(57) # Acrescenta item aos poucos dentro da lista
print(nova_lista)