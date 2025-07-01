soma = 0
tot = 0
for con in range(1, 7):
    num = int(input('Digite o {}º valor: ' .format(con)))
    if num % 2 == 0:
        soma+=num
        tot += 1

print('Você informou {} numeros PARES e a soma foi {}' .format(tot, soma))
