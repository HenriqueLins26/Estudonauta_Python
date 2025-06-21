peso = float(input('qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))

imc = peso / (altura ** 2)
print('O IMC dessa peso é de {:.1f}' .format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, Você esta na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print("Você está em Sobrepeso")
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')

