sn = ''
tot = soma = maior = menor = 0

while sn != 'N':
    n1 = int(input('Digite um número: '))

    tot += 1
    soma += n1

    if tot == 1:
        maior = n1
        menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1

    sn = str(input('Quer continuar? [S/N] ')).upper().split()[0]

med = soma / tot

print('Você digitou {} números e a média foi {:.2f}' .format(tot, med))
print('O maior valor foi {} e o menor foi {}' .format(maior, menor))