'''beecrowd | 1002
Área do Círculo
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1'''

'''A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159:

- Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.'''


raio=float(input())

A=3.14159*(raio**2)

print('A={:.4f}'.format(A))
