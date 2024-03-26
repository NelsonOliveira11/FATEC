a = float(input('Qual o valor do lado 1?'))
b = float(input('Qual o valor do lado 2?'))
c = float(input('Qual o valor do lado 3?'))

if (a > (c+b)) or (b > (a+c)) or (c > (b+a)):
    triangulo= True
else:
    triangulo= False

if (triangulo):
    print('Os Valores formam um triângulo')

if (a==b) and (c==a):
    tipo= "Equilatero"
elif (a==b) or (c==a) or (b==c):
    tipo= "Isósceles"
else:
    tipo="Escaleno"

print("O tipo do triângulo é:", tipo)