alt = float(input('Qual a altura da parede? '))
lar = float(input('Qual a largura da parede? '))

tot = alt * lar

print('Sua parede tem a dimensão de {} x {} e sua área é de {:.2f}m². ' . format(alt, lar, tot,))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta' .format(tot / 2))
