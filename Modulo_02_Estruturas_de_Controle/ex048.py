soma = 0
tot = 0

for cont in range(1, 501):
    if cont % 3 == 0:
        soma += cont
        tot += 1

print('A soma de todos os {} valores solicitados é {}'.format(tot, soma))
