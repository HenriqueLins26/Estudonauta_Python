print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)

t1 = float(input('Primeiro segmento: '))
t2 = float(input('Segundo segmento: '))
t3 = float(input('Terceiro segmento: '))

if t1 + t2 > t3 and t1 + t3 > t2 and t2 + t3 > t1:
    tri = 'PODEM FORMAR'
else:
    tri ='NÃO PODEM FORMAR'

print('Os segmentos acima {} triângulo! ' .format(tri))
