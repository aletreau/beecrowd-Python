
z=int(input())

if z >= 100:
    print((z//100), "nota(s) de R$ 100,00")

    z = z%100

if z >= 50:
    print((z//50), "nota(s) de R$ 50,00")

    z = z%50
if z >= 20:
    print((z//20), "nota(s) de R$ 20,00")

    z = z%20
if z >= 10:
    print((z//10), "nota(s) de R$ 10,00")

    z = z%10
if z >= 5:
    print((z//5), "nota(s) de R$ 5,00")
    z = z%5
    
if z >= 2:
    print((z//2), "nota(s) de R$ 2,00")
    z = z%2

if z >= 1:
    print((z//1), "nota(s) de R$ 1,00")

    z = z%1
    