'''Distância Entre Dois Pontos
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1'''
import math
from posixpath import split



x1, x2= input().split()
y1, y2= input().split()
print(x1," ",x2," ",y1," ",y2)



D= math.sqrt(((float(x2) - float(x1))*(float(x2) - float(x1))) - ((float(y2)-float(y1)) *(float(y2)-float(y1))))

print("%0.4f" %D)