from time import localtime

ano = int(input('Ano de nascimento: '))
atual = localtime().tm_year

idade = atual - ano

print('O atleta tem {} anos.' .format(idade))

if idade <= 9:
    cla = "Mirim"
elif idade <= 14:
    cla = "Ifantil"
elif idade <=19:
    cla = "Junior"
elif idade <= 25:
    cla = "Sênior"
else:
    cla = "Master"

print('Classificação: {}' .format(cla))
