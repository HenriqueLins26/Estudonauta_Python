n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 >n1:
    pode = "PODEM FORMAR"
    if n1 == n2 == n3:
        tipo = "Equilatero"
    elif n1 == n2 or n3 == n2 or n1 == n3:
        tipo = "Isosceles"
    else:
        tipo = "Escaleno"
else:
    pode = "NÃO PODEM FORMAR"
    tipo = ""

print('Os segmentos acima {} um triângulo {} ' .format(pode, tipo))
