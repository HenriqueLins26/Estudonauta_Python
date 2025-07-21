n = int(input('Digite um número para calcular se Fatorial: '))

c = n
f = 1

print('Calculando {}! = '.format(n), end='')

while c > 0:
    print(c, end='')

    f *= c
    c -=1
    if c > 0:
        print(' x ', end='')
    else:
        print(' = ', end='')

print(f)
