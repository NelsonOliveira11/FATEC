valor_da_hora = int(input('Quanto você ganha por hora trabalhada?'))
horas_trabalhadas = int(input('Quantas horas você trabalha mensalmente?'))
salario_bruto = float(valor_da_hora*horas_trabalhadas)
valor_inss = float(salario_bruto*(10/100))
valor_fgts = float(salario_bruto*11/100)
valor_sindicato = float(salario_bruto*(3/100))




if (salario_bruto <= 900):
    ir = 0
    aliquota = 0
elif salario_bruto <= 1500:
    ir= salario_bruto*0.05
    aliquota= 5
elif salario_bruto <= 2500:
    ir =salario_bruto*0.1
    aliquota = 10
elif salario_bruto > 2500:
    ir = salario_bruto*0.2
    aliquota = 20

descontos = float(ir+valor_inss)

print('Salario Bruto:(', valor_da_hora, '*', horas_trabalhadas,'):       R$', salario_bruto)
print('(-) IR (',aliquota,'%):                   R$', ir)
print('(-)INSS:(','10%):                  R$', valor_inss)
print('FGTS:(','11%):                     R$', valor_fgts)
print('Desconto Sindicato:(','3%):        R$', valor_sindicato)
print('Total de descontos:              R$', ir+valor_fgts)
print('Salário Líquido:                 R$', salario_bruto-descontos)


