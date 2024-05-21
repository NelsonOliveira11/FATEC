def total_bixos(t_cabec, t_pes):
    pes_a_mais = t_cabec * 4 - t_pes
    t_pes -= pes_a_mais
    t_coelho = t_pes // 4
    t_patos = t_cabec - t_coelho
    return [t_patos, t_coelho]


cabecas = int(input('Total de cabeças: '))
pes = int(input('Total de pés: '))
bixos = total_bixos(cabecas, pes)

print(f'''
Total de patos: {bixos[0]}
Total de coelhos: {bixos[1]}
''')