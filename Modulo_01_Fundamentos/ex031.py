dist = float(input('Qual a distancia da sua viagem? '))
print('Você estar prestes a começar uma viagem de {}Km.' .format(dist))

if dist > 200:
    pas = dist * 0.45
else:
    pas = dist * 0.50

print('E o preço da sua passagem será de R${:.2f}'.format(pas))
