geral = []
nome_peso = []
maior = menor = 0

while True:
    nome_peso.append(str(input("Nome: ")))
    nome_peso.append(float(input("Peso: ")))
    geral.append(nome_peso[:])

    if len(geral) == 1:
        maior = menor = nome_peso[1]
    else:
        if nome_peso[1] > maior:
            maior = nome_peso[1]
        if nome_peso[1] < menor:
            menor = nome_peso[1]

    nome_peso.clear()

    sn = str(input("Quer continuar? [S/N] ")).strip().upper()
    if sn == 'N':
        break

print("-=" * 20)
print(f"Ao todo, você cadastrou {len(geral)} pessoas.")

print(f"O maior peso foi de {maior:.1f}Kg. Peso de ", end='')
for g in geral:
    if g[1] == maior:
        print(f"[{g[0]}]", end=" ")
print()

print(f"O menor peso foi de {menor:.1f}Kg. Peso de ", end='')
for g in geral:
    if g[1] == menor:
        print(f"[{g[0]}]", end=" ")
print()
