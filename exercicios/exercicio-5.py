# -*- coding: utf-8 -*-

# EXERCÍCIO 5 - operacao MATEMÁTICA #

# Definindo variáveis

n1 = int(input("Digite o 1º número: \n"))
n2 = int(input("Digite o 2º número: \n"))
operacao = input("Digite o sinal da operacao que deseja realizar? \n" + "(+) Adição;	(-) Subtração;	(x) Multiplicação;	(/) Divisão;	(^) Exponenciação;	\n")

# Definindo funções

def soma(n1, n2):
	return n1 + n2

def subtracao(n1, n2):
	return n1 - n2

def multiplicacao(n1, n2):
	return n1 * n2

def divisao(n1, n2):
	return n1 / n2

def exponenciacao(n1, n2):
	return n1 ** n2

# Define as condições

if operacao == "+":
	print(soma(n1,n2))

elif operacao == "-":
	print(subtracao(n1,n2))

elif operacao == "x":
	print(multiplicacao(n1,n2))

elif operacao == "/":
	print(divisao(n1,n2))

else:
	print(exponenciacao(n1,n2))
