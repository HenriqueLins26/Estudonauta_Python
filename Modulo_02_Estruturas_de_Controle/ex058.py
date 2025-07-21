from random import randint
sor = randint(0,10)
tot = 0
acertou = False

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')

while not acertou:
    ten = int(input('Qual o seu palpite? '))
    tot += 1

    if ten == sor:
        acertou = True
    else:
        if sor > ten:
            print('Mais... Tente mais uma vez.')
        elif sor < ten:
            print('Menos.. Tente mais uma vez')

print('Acertou com {} tentativas. Parabens!' .format(tot))