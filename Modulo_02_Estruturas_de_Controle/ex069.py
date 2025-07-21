print('-'*25)
print('Cadastre uma Pessoa')

tot = totmas = totfem = 0

while True:
    print('-' * 25)
    idade = int(input('Idade: '))

    if idade >= 18:
        tot +=1

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 25)

    if sexo == 'M':
        totmas += 1
    elif sexo == 'F' and idade < 20:
        totfem += 1

    sn = ' '
    while sn not in 'SN':
        sn = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if sn == 'N':
        break

print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {tot}')
print(f'Ao todo temos {totmas} homens cadastrados')
print(f'E temos {totfem} mulheres com menos de 20 anos')
