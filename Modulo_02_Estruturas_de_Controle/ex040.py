nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

med = (nota1 + nota2) / 2

print('Tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}' .format(nota1, nota2, med))

if med >= 7.0:
    situ = "APROVADO"
elif 7 > med >= 5:
    situ = "em RECUPERAÇÃO"
else:
    situ = "REPROVADO"

print('O aluno está {}' .format(situ))
