

salario = float(input('Qual o valor do seu salário?'))
ajuste = float(input('Digite a porcentagem de ajuste:'))
salario_com_aumento = salario+(salario*(ajuste/100))
ajuste_em_dinheiro = float(salario_com_aumento-salario)

print(f'Seu salário atual é de:R${salario:8.2f}')
print(f'Você recebeu um aumento de:R${ajuste_em_dinheiro:8.2f}')
print(f'Seu salário após o aumento é de:R$ {salario_com_aumento:8.2f}')
print(f'Sua porcentagem de aumento foi de:{ajuste:1.0f}%')