print('_'*30)
print('    Sequência de Fibonacci')
print('_'*30)

ter = int(input('Quantos termos você quer mostrar? '))

n1 = 0
n2 = 1
c = 1

print('~'*30)

while c <= ter:
    print(n1, end=' → ')
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    c += 1
print('FIM')
print('~'*30)
