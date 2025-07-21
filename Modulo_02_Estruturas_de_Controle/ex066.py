soma = c = 0

while True:
    n1 = int(input('Digite um valor (999 para parar): '))
    if n1 == 999:
        break
    c+=1
    soma += n1

print(f'A soma dos {c} valores foi {soma}!')
