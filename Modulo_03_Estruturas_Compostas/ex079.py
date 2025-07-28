lista = []

while True:
    num = int(input("Digite um valor: "))

    if num in lista:
        print("Valor duplicado! Não vou adicionar...")
    else:
        print("Valor adicionado com sucesso...")
        lista.append(num)

    opc = str(input("Quer continuar? [S/N] ")).strip().upper()
    if opc == 'N':
        break

print("-="* 30)
lista.sort()
print(f"Você digitou os valores {lista}")
