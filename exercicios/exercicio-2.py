# -*- coding: utf-8 -*-

# EXERCÍCIO 2 - BOLETIM DIGITAL#

nota1 = float(input("Digite a 1ª nota:  \n"))
nota2 = float(input("Digite a 2ª nota: \n"))
media_escolar = 6.0

def media(nota1, nota2):
	return (nota1 + nota2) / 2

nota_final = media(nota1, nota2)

if nota_final >= media_escolar:
 	print("Você está aprovado! Parabéns!")
else:
	print("Reprovado! Volte à estudar, seu burro!")