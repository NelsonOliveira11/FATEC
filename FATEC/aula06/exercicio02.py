bruto = float(input('Valor total da compra:'))

if bruto <= 1000:
    desconto=bruto*0.1
    print('O desconto é de 10%:(R$',desconto,')')
if bruto <= 5000:
    desconto=bruto*0.2
    print('O desconto é de 20%:(R$',desconto,')')
if bruto > 5000:
    desconto=(bruto*0.3)
    print('O desconto é de 30%:(R$',desconto,')')
