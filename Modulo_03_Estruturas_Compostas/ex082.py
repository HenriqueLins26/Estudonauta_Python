lista, par, impar = [], [], []

while True:
    num = int(input("Digite um número: "))
    lista.append(num)

    if num  % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

    opc = str(input("Quer continuar? [S/N] ")).strip().upper()
    if opc == 'N':
        break

print("-="*30)
print(f"A lista completa é {lista}")
print(f"A lista de pares {par}")
print(f"A lista de ímpares {impar}")
