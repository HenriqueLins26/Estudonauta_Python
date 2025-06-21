from time import localtime
atual = localtime().tm_year

ano = int(input('Ano de nascimento: '))
ida = atual - ano

print('Quem nasceu em {} tem anos {} em {}' .format(ano, ida, atual))
te = ano + 18

if ida == 18:
    print('Você tem que se alistar IMEDIATAMENTE.')
elif ida > 18:
    fal = atual - te
    print('Você deveria se alistado há {} anos.' .format(fal))
    print('Seu alistamento foi em {}'.format(te))
else:
    fal = te - atual
    print('Ainda falta {} anos para o alistamento' . format(fal))
    print('Seu alistamento será em {}' .format(te))
