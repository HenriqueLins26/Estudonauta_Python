lista = []

while True:
    lista.append(int(input("Digite um número:")))

    opc = str(input("Quer continuar? [S/N] ")).strip().upper()
    if opc == 'N':
        break

lista.sort(reverse=True)

print("-="*30)
print(f"Você digitou {len(lista)} elementos.")
print(f"Os valores em ordem decrescente são {lista}")
print("O valor 5 ", end='')
if 5 in lista:
    print("faz parte da lista!")
else:
    print("não foi encontrado na lista!")
