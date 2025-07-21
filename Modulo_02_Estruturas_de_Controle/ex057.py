sx = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

#while sx != 'M' and sx != 'F':
while sx not in 'MF':
    sx = str(input('Dados inválidos. Por favor, informe o seu sexo: ')).strip().upper()[0]

print('Sexo {} registrado com sucesso' .format(sx))
