print('='*10, ' LOJA SEILÁ ', '='*10)
valor = float(input('Preço das compras R$'))

print('''FORMAS DE PAGAMENTO
[1] á vista dinheiro/cheque
[2] á vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opc = int(input('Qual é a opção? '))

if opc == 1:
    desc = valor - (valor * 10 / 100)
elif opc == 2:
    desc = valor - (valor * 5 / 100)
elif opc == 3:
    desc = valor / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS' .format(desc))
elif opc == 4:
    desc = valor + (valor * 20 /100)
    par = int(input('Quantas parcelas? '))
    vezes = desc / par
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS' . format(par, vezes))
else:
    print('Opção Invalida')
    desc = valor

print('Sua compra de R${:.2f} vai custar R${:.2f} no final' .format(valor, desc))
