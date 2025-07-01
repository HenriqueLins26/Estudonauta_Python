print('='*30)
print('     10 TERMOS DE UMA PA      ')
print('='*30)

n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão: '))
tot = n1 + (10 -1) *  n2

for c in range(n1, tot + n2, n2):
        print(c ,'-> ' , end='')
print('ACABOU')
