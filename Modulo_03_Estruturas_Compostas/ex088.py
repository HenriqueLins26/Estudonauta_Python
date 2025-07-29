from random import randint
from time import sleep

lista = []
mega = []

print("-"* 30)
print(f"{'JOGA NA MEGA SENA':^30}")
print("-"* 30)

num = int(input("Quantos jogos você quer que eu sorteie? "))
print(f"{'-=' * 3} SORTEANDO {num} JOGOS {'-='* 3}")

for vezes in range(1, num+1):
    while (len(mega) <
           6):
        sorteado = randint(1, 60)
        if sorteado not in mega:
            mega.append(sorteado)

    mega.sort()
    lista.append(mega[:])
    mega.clear()

for i, jogo in enumerate(lista):
    print(f"Jogo {i+1}: {jogo}")
    sleep(1)

print(f"{'-=' * 5} < BOA SORTE {'-=' * 5}")