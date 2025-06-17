vel = float(input('Qual é a sua velocidade atual do carro? '))

if vel > 80:
    print('Multado! Você execedeu o limete permitido que é 80Km/h')
    multa = (vel - 80) * 7
    print('Você deve pagar uma de R${:.2f}!' . format(multa))

print('Tenha um bom dia! Dirija com segurança!')
