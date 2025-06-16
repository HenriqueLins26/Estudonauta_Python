val = float(input('Qual o valor do produto? R$'))

des = val - (val * 5 / 100)

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(val, des))
