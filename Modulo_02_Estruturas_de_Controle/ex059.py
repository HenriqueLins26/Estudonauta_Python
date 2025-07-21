from time import sleep
opc = 0

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

while opc != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros 
    [5] sair do programa''')

    opc = int(input('>>>> Qual é a sua opção? '))

    if opc ==1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}' .format(n1, n2, soma))
    elif opc == 2:
        pro = n1 * n2
        print('A multiplicação entre {} x {} é {}' .format(n1, n2, pro))
    elif opc == 3:
        if n1 > n2:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n1))
        elif n2 > n1:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n2))
        else:
            print('O primeiro numero {} e o segundo numero {} são iguais' .format(n1, n2))
    elif opc == 4:
        print('Informe os numeros novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opc == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção invalida. Tente novamente')
    print('=-='*10)

print('Fim do programa! Volte sempre!')