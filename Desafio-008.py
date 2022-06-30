'''beecrowd | 1020
Idade em Dias'''

dias=int(input())

print((dias//365),"Ano (s)")
print(((dias)-(365*(dias//365)))//30,"Mês (es)")
print(((dias)-(365*(dias//365)))%30,"Dia (s)")

