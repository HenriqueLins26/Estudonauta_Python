totidade = 0
maior = 0
velho = ''
totfem = 0

for p in range(1, 5):
    print('----- {}ª PESSOA -----' .format(p))

    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]')).upper()

    if sexo == 'M':
        maior = idade
        velho = nome
    else:
        if idade > maior:
            maior = idade
            velho = nome

    if sexo == 'F':
        if idade < 20:
            totfem += 1

    totidade += idade

media = totidade / 4
print('A média de idade do grupo é de {:.1f} anos' .format(media))
print('O homem mais velho tem {} anos e se chama {}.' .format(maior, velho))
print('Ao todo são {} mulheres com menos de 20 anos' .format(totfem))
