# -*- coding: utf-8 -*-

# EXERCÍCIO 3 - EQUAÇÕES DE 2º GRAU #

a = int(input("Digite o valor de A: \n"))
b = int(input("Digite o valor de B: \n"))
c = int(input("Digite o valor de C: \n"))

delta = b**2-4*a*c
print(delta)

raiz_delta = delta**0,5
print(raiz_delta)

x1 = (-b + raiz_delta) / (2*a)
x2 = (-b - raiz_delta) / (2*a)

print(x1)
print(x2)