from math import radians, sin, cos, tan

n1 = float(input('Digite o ângulo que você deseja: '))

ang = radians(n1)
se = sin(ang)
co = cos(ang)
ta = tan(ang)

print("O ângulo de {} tem o SENO de {:.2f}" .format(n1, se))
print("O ângulo de {} tem o COSSENO de {:.2f}" .format(n1, co))
print("O ângulo de {} tem o TANGENTE de {:.2f}" .format(n1, ta))
