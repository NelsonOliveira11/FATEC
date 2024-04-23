lista = []
x = int(input("Numero 1:"))
y = int(input("Numero 2:"))
z = int(input("Numero 3:"))

lista.append(x)
lista.append(y)
lista.append(z)
lista.sort(reverse=True)

print(f'Numeros em ordem decrescente:', lista)

