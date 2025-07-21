print('Gerador de PA')
print('-='*10)

n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão da PA: '))

te = n1
c = 1
tot = 0
mais = 10

while mais != 0:
    tot += mais
    while c <= tot:
        print(te, end=' → ')
        te += n2
        c +=1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.' .format(tot))
