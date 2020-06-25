# -*- coding: utf-8 -*-

# Orientação à objetos (strings parte 1) #

nome = "Marcelo"
sobrenome = "Goulart Rodrigues Junior"
concatenacao = nome + " " + sobrenome
tamanho = len(concatenacao)

print(tamanho) # conta quantos caracteres tem numa string
print(nome[2]) # imprime qual caractere está na 2ª posição da string
print(concatenacao[0:7]) # exibe na tela os caracteres em sequênncia desde o 1º caractere até o último
print("Seu nome é: \n" + concatenacao)