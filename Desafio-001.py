#A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo
#1048
#https://www.beecrowd.com.br/judge/pt/problems/view/1048
'''Salário	Percentual de Reajuste
0 - 400.00              15%
400.01 - 800.00         12%
800.01 - 1200.00        10%
1200.01 - 2000.00       7%
Acima de 2000.00        4%
'''

'''
salario = s
reajuste = r
percentual = p
'''

#x = float(input())
#x = "{:.2f}".format(float(input()))


x = float(input())


if  0 <= x <=  400.00:
    s = x * 1.15
    r = s - x
    p=15
    
elif 400.01 <= x <= 800.00:
    s  = x * 1.12
    r = s - x
    p=12
    
elif 800.01 <= x <=  1200.00:
    s = x * 1.10
    r = s - x
    p=10
    
elif 1200.01 <= x <= 2000.00:
    s = x*1.07
    r = s-x
    p=7
    
elif x > 2000.00:
    s = x*1.04
    r = s-x
    p=4
            

print(('Novo Salario: {:.2f}'.format(s)),('\nReajuste ganho: {:.2f}'.format(r)),'\nEm percentual: ',p,'%')



#print(('Novo Salario: {:.2f}'.format(s)),('\nReajuste ganho: {:.2f}'.format(r)),('\nEm percentual: {} %'.format(p)))




#print('Em percentual: {} %'.format(p))





