num = int(input('Digite um número: '))
tot = 0

for c in range(1, num+1):
    if num % c == 0:
        print('({})' .format(c),end=' ')
        tot +=1
    else:
        print(c,end=' ')

print('\nO numero {} foi divisivel {} vezes' .format(num, tot))
if tot == 2:
    print("E por isso ele É PRIMO")
else:
    print("E por isso ele NÂO É PRIMO")
