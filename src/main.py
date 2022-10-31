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

