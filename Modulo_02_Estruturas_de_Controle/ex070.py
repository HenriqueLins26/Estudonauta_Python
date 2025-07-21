print('_' * 30)
print('     LOJA SUPER BARATÃO')
print('_' * 30)

tot = caro = barato = c = 0
probarato = ""

while True :
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    tot += preco
    c += 1

    if c == 1:
        barato = preco
        probarato = produto
    else:
        if preco < barato:
            barato = preco
            probarato = produto


    if preco >= 1000.00:
        caro += 1

    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if cont == 'N':
        break
print('---------- FIM DO PROGRAMA ----------')
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {caro} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {probarato} que custa RS{barato:.2f}')
