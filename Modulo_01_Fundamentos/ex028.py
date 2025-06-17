from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

sort = randint(0, 5)

tent = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)

if tent == sort:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!' .format(sort, tent))
