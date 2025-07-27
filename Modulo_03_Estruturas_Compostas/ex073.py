times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
        'Atlético-MG', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
        'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará SC',
        'Vasco da Gama', 'Sport Recife','América-MG', 'EC Vitória', 'Paraná')

print('-='* 15)
print(f"Lista de times do Brasileirão: {times}")

print('-='* 15)
print(f"Os 5 primeiros são {times[0:5]}")

print('-='* 15)
print(f"Os 4 últimos são {times[-4:]}")

print('-='* 15)
print(f"Times em ordem alfabética: {sorted(times)}")

print('-='* 15)
print(f"O Chapecoense esta na {times.index("Chapecoense") + 1}ª posição")
