from time import sleep
from random import randint

item = ('Pedra', 'Papel', 'Tesoura')
sor = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''' ,)
num = int(input('Qual é a sua jogada? '))

sleep(0.3)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('-='*11)
print('Computador jogou {}' .format(item[sor]))
print('Jogador jogou {}' .format(item[num]))
print('-='*11)

if sor == 0:
    if num == 0:
        print('EMPATE')
    elif num == 1:
        print('JOGADOR VENCEU!')
    elif num == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVALIDA!')
elif sor == 1:
    if num == 0:
        print('COMPUTADOR VENCEU')
    elif num == 1:
        print('EMPATE')
    elif num == 2:
        print('JOGADOR VENCEU!')
    else:
        print('JOGADA INVALIDA!')
elif sor == 2:
    if num == 0:
        print('JOGADOR VENCEU!')
    elif num == 1:
        print('COMPUTADOR VENCEU')
    elif num == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA!')
