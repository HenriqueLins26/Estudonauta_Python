from time import localtime

atual = localtime().tm_year
maior = 0
menor = 0

for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? ' . format(c)))
    soma = atual - ano
    if soma >= 18:
        maior += 1
    else:
        menor += 1

print('Ao todo tivemos {} pessoas maiores de idade' .format(maior))
print('E também tivemos {} pessoas menores de idade' .format(menor))
