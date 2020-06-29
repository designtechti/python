# -*- coding: utf-8 -*-

# PYTHON AVANÇADO: Função list comprehension #

x = [1, 2, 3, 4, 5]
y = []

# Eleva a lista x ao quadrado (x²) da forma mais simples

for i in x:
	y.append(i**2)
print(y)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

# Eleva a lista x ao quadrado (x²) com o list comprehension s/ condição

x = [1, 2, 3, 4, 5] # lista
y = [i**2 for i in x ] # [valor_a_adicionar laço]

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

# Adiciona apenas os nº ímpares da lista x

x = [1, 2, 3, 4, 5] # lista
y = [i**2 for i in x ] # [valor_a_adicionar condição]
z = [i for i in x if i%2==1]

print(z)