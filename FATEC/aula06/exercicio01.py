num = int(input('Digite o número:'))

if int(num/5)*5==num and int(num/3)*3==num:
    divisivel:True
    print('O número é divisível por 5 e 3')
else:
    print('O número não é divisível por 5 e 3')