nota1 = float(input('Qual a nota numero 1?'))
nota2 = float(input('Qual a nota numero 2?'))
media = (nota1+nota2)/2

if media <= 4:
    conceito = 'E'
    aprovado= False
elif media <=6:
    conceito = 'D'
    aprovado= False
elif media <=7.5:
    conceito = 'C'
    aprovado= True
elif media <= 9:
    conceito = 'B'
    aprovado= True
elif media <= 10:
    conceito = 'A'
    aprovado = True

if (aprovado):
    print('Aprovado')
else:
    print('Reprovado')


print('Notas:',nota1,',', nota2)
print('Média:',media)
print('Conceito:',conceito)
