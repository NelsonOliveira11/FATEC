def eh_primo(num):
    primos = [2, 3, 5, 7, 11]
    if num in primos:
        return True
    for i in primos:
        if num % i == 0 or num == 1:
            return False
    return True


def qnt_num_primos(num):
    array = []
    i = 0
    while len(array) != num:
        if eh_primo(i):
            array.append(i)
        i += 1
    return array


y = 14
lista = qnt_num_primos(y*2+5)
soma = 0
for dig in lista:
    soma += dig

print(f'''
{y} * 2 + 5 = {y * 2 + 5}
Lista: {lista}
Valor da Soma de Todos os Números: {soma}
''')