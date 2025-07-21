print('Gerador de PA')
print('-='*10)

n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão da PA: '))
r1 = n1
tot = 1

while tot <= 10:
    print(r1, end=' → ')
    r1 += n2
    tot+=1
print('FIM')
