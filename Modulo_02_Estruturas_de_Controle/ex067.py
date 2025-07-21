while True:
    n1 =int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 35)

    if n1 < 0:
        break

    #c = 1
    #s = 0

    #while c <= 10:
       # s = c * n1
    for c in range(1, 11):
        print(f'{c} x {n1} = {c * n1}')
        #c += 1

    print('-' * 35)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')