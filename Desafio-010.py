'''beecrowd | 1035
Teste de Seleção 1'''

'''Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D 
for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, 
ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", 
senão escrever "Valores nao aceitos".'''

from posixpath import split

A,B,C,D= input().split()


if (B>C) and (D>A) and ((C+D)>(A+B)) and (int(C) >= 0)  and  (int(D) >= 0) and (int(A)%2==0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")


