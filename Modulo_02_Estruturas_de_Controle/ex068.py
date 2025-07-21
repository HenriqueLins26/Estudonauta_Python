from random import randint

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)

vitoria = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    soma = jogador + computador

    esc = ' '
    while esc not in 'PI':
        esc = str(input('PAR ou Ímpar? [P/I] ')).strip().upper()[0]

    if soma % 2 == 0:
        pi = "PAR"
    else:
        pi = "ÍMPAR"

    print('_' * 55)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} deu {pi}')
    print('_' * 55)

    if (soma % 2 == 0 and esc == 'P') or (soma % 2 == 1 and esc == 'I'):
        print('Você VENCEU!')
        vitoria += 1
        print('Vamos jogar novamente...')
    else:
        print('Você PERDEU!')
        break

print('=-' * 15)
print(f'GAMER OVER! Você venceu {vitoria} vezes.\n')
