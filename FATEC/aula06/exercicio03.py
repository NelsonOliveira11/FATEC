med1 = float(input('Qual a largura do aposento em metros?'))
med2 = float(input('Qual a comprimento do aposento em metros?'))
area = (med1*med2)
parede1 = 2.80*med1
parede2 = 2.80*med2
parede3 = (2.80*med2)-1.68
m2paredes = parede1+parede1+parede2+parede3
litros = m2paredes/3
galao18 = int(litros/18)
galao3_7 = int(litros/3.7)
galao1 = int(litros/1)
sobra = litros-(galao18*18)



print('A quantidade de tinta necessária é de:', litros, 'litros.')
print('que equivalem a', galao18, 'galoes de tinta de 18L', int(sobra/3.7) ,'galões de 3.7 litros', int(sobra/3.7)/1, 'galoes de 1 litro')

