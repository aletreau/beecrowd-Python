
z=576.73

if z >= 100:
    print(int((z//100)), "nota(s) de R$ 100,00")

    z = z%100

if z >= 50:
    print(int((z//50)), "nota(s) de R$ 50,00")

    z = z%50
if z >= 20:
    print(int((z//20)), "nota(s) de R$ 20,00")

    z = z%20
if z >= 10:
    print(int((z//10)), "nota(s) de R$ 10,00")

    z = z%10
if z >= 5:
    print(int((z//5)), "nota(s) de R$ 5,00")
    z = z%5
    
if z >= 2:
    print(int((z//2)), "nota(s) de R$ 2,00")
    z = z%2

if z >= 1:
    print(int((z//1)), "nota(s) de R$ 1,00")

    z = z%1
    
if z >= 0.50:
    print(int((z//.5)), "moeda(s) de R$ 0.50")

    z = z%.5
    
    
if z >= 0.10:
    print(int((z//.10)), "moeda(s) de R$ 0.10")

    z = z%.10
    
if z >= 0.01:
    print(int((z//.01)), "moeda(s) de R$ 0.01")

    z = z%.01
    