me = float(input('Distancia em metros: '))

print('A media de {}m corresponde a' . format(me))
print('{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format((me/1000), (me/100), (me/10), (me*10), (me*100), (me*1000)))