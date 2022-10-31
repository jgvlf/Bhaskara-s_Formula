from math import pow, sqrt
from sys import exit

a = int(input("Digite o valor do coeficiente \"a\": "))
b = int(input("Digite o valor do coeficiente \"b\": "))
c = int(input("Digite o valor do coeficiente \"c\": "))

if(a < 0):
    ordem_gráfico = "O gráfico é decresente."
else:
    ordem_gráfico = "O gráfico é crescente."
