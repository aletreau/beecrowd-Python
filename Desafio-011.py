'''Fórmula de Bhaskara
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. 
Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”,
caso haja uma divisão por 0 ou raiz de numero negativo.'''

A, B, C = input().split()

print(A, B, C)

print(float(B)**2)
print(4*float(A))
print((-4*float(A))*float(B))
delta = (float(B)**2) - 4*float(A)*float(B)

#delta = delta = (b ** 2) - 4 * a * c


print(delta)