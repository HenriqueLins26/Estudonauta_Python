din = float(input('Quanto dinheiro você tem na carteira? R$'))

dol = din / 5.81

print('Com R${:.2f} você pode comprar US${:.2f}' .format(din, dol))
