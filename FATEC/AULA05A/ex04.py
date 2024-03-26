import math

print('Calculo de equação de segundo grau')
print('ax2 + bx + c = 0')

a = float(input('Informe o valor de A:'))
if a==0:
    print('Esta não é uma equação de segundo grau.')
else:
    delta=b*b-(4*a*c)

if delta<0:
    print('A equação não possui valores reais')
elif delta==0:
    print('A equação possui apenas uma raíz')
    raiz = -(b)/(2*a)
    print("Raiz:", raiz)
else:
    print("A equação possui duas raízes")
    raiz1= -(b) + (delta*delta) / 2*a
    raiz2= -(b) - (delta*delta) / 2*a
    print("Raiz 1:", raiz1)
    print("Raiz 2:", raiz2)