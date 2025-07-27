from random import randint

c = 1
num = ()
maior = menor = 0

while c <= 5:
    sorteado = randint(1, 10)
    num += (sorteado, )

    #if c == 1:
    #    maior = sorteado
    #    menor = sorteado
    #else:
    #    if sorteado > maior:
   #         maior = sorteado
    #    if sorteado< menor:
    #        menor = sorteado
    c+=1
print(f"Os valores sorteados foram: {' '.join(map(str, num))}")
#print(f"O maior valor sorteado foi {maior}")
#print(f"O menor valor sorteado foi {menor}") ou
print(f"O maior valor sorteado foi {max(num)}")
print(f"O menor valor sorteado foi {min(num)}")
