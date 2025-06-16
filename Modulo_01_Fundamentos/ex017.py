from math import hypot

n1 = float(input("Comprimento do cateto oposto: "))
n2 = float(input("Comprimento do cateto adjacente: "))

soma = hypot(n1, n2)
#soma = sqrt(n1**2 + n2**2)
#soma = (n1**2 + n2**2) ** (1/2)

print("A hipotenusa vai medir {:.2f}" .format(soma))
