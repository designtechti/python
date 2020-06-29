# -*- coding: utf-8 -*-

# EXERCÍCIO 5 - operacaoERAÇÃO MATEMÁTICA #

# Definindo variáveis

n1 = int(input("Digite o primeiro número: "))
sinal = input("Digite o sinal: ")
n2 = int(input("Digite o segundo número: "))
	 
# Definindo condições

if sinal == "+":
	operacao = n1 + n2
 
elif sinal == "-":
	operacao = n1 - n2
 
elif sinal == "/":
	operacao = n1 + n2
 
elif sinal == "*":
	operacao = n1 * n2
 
else:
	print("Sinal inválido.")

# Exibe na tela o resultado
	 
print(operacao)
