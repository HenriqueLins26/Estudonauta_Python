num = int(input('Digite um número: '))

print('Escolha uma das bases para converção')
print('[1] converter para BINARIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')
opc = int(input('Sua opção: '))

if opc == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opc == 2:
    print('{} convertido para OCTAL é igual a {}' .format(num,oct(num)[2:]))
elif opc == 3:
    print('{} convertido para HEXADECIMAL é igual a {}' .format(num, hex(num)[2:]).upper())
else:
    print('Opção inválida. Tente novamente!')
