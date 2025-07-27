num = ('zero', 'um', 'dois', 'três', 'quatro',
       'cinco', 'seis', 'sete', 'oito', 'nove',
       'dez', 'onze', 'doze', 'treze', 'quatorze',
       'quinze', 'dezesseis', 'dezesete', 'dezoito',
       'dezenove', 'vinte')

for c in range(1):
    esco = int(input('Digite um numero entre 0 e 20: '))
    while esco < 0 or esco > 20:
        esco = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    if esco >= 0 or esco <= 20:
        print(f'Você digitou o numero {num[esco]}')
