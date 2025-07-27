lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
         'Estojo', 25.90, 'Tranferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90)

print('_' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('_' * 40)

i = 0
for c in lista[0::2]:
    print(f"{lista[i]:.<30}R${lista[i+1]:>7.2f}")
    i += 2

print('_' * 40)
