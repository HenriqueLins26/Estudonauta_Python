dig = str(input("Digite uma frase: ")).strip().upper()

print("A letra A aparece {} vezes na frase." .format(dig.count('A')))
print("A primeira letra A apareceu na posição {}" .format(dig.find('A') + 1))
print("A última letra A apareceu na posição {}" .format(dig.rfind('A') + 1))
