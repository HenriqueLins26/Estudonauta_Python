#n1 = 0
#tot = 0
#soma = 0
#ou
n1 = tot = soma = 0

while n1 != 999:
    n1 = int(input('Digite um número [999 para parar] '))
    if n1 != 999:
        soma += n1
        tot += 1

print('Você digitou {} números e a soma entre eles foi {}' .format(tot, soma))
