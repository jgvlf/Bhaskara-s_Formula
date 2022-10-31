from math import pow, sqrt
from sys import exit

a = int(input("Digite o valor do coeficiente \"a\": "))
b = int(input("Digite o valor do coeficiente \"b\": "))
c = int(input("Digite o valor do coeficiente \"c\": "))

if(a < 0):
    ordem_gráfico = "O gráfico é decresente."
else:
    ordem_gráfico = "O gráfico é crescente."

delta = pow(b, 2)-4*a*c

if(delta > 0):
    qtd_raizes = "Possui 2 raizes."
elif(delta == 0):
    qtd_raizes = "Possui apenas 1 raiz."
else:
    qtd_raizes = "Não possui raizes."

xv = -b/2*a

if(delta == 0):
    yv = delta/4*a
else:
    yv = -delta/4*a

if(delta < 0):
    print("\n")
    print("Resultado da expressão reduzida do segundo grau: ")
    print(ordem_gráfico)
    print(f"O \"X\" do vértice é: {xv}, e o \"Y\" do vértice é {yv}.")
    print(f"Portanto a coordenada do vétice é: ({xv}, {yv})")
    print(qtd_raizes)
    print("\n")
    exit(0)


