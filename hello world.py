# -*- coding: utf-8 -*-

# Orientação à objetos (strings parte 2) #

nome = "Marcelo \n"
sobrenome = "Goulart Rodrigues Junior"
concatenacao = nome + " " + sobrenome
busca = concatenacao.find("Rodrigues")

print(concatenacao.lower()) # Método que deixa a string com caixa baixa
print(concatenacao.upper()) # Método que deixa a string com caixa alta
print(concatenacao.strip()) # Método que deixa a string sem espaços e caracteres especiais
print(concatenacao.split()) # Método que converte a string em uma lista
print(busca) # Método que faz uma busca na string de acordo com o trecho que se deseja encontrar
print(concatenacao[busca:]) # Método que exibe na tela o resultado da busca desde o trecho que foi encontrado até o fim
print(concatenacao.replace("Rodrigues", "Silva")) # Método que substitui trecho de string por outro valor