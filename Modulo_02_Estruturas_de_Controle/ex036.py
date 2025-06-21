casa = float(input('Valor da casa: R$'))
sal = float(input('Salario do comprador: R$'))
ano = int(input('Quantos anos de financiamento? '))

emp = casa / (12 * ano)
min = sal * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}' .format(casa, ano, emp))

if emp <= min:
    print('Empréstimo pode sere CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
