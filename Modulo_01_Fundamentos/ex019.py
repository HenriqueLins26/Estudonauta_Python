from random import  choice
# usa se randint para sortear números

no1 = str(input("Primeiro aluno: "))
no2 = str(input("Segundo aluno: "))
no3 = str(input("Terceiro aluno: "))
no4 = str(input("Quarto aluno: "))

sor = choice([no1, no2, no3, no4])
#ou usar uma variavel como
#lista = [no1, no2, no3, no4]
#sor = choice(lista) => sorteia palavras

print("O aluno escolhido foi {}" .format(sor))
