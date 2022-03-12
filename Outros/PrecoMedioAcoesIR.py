from pandas import read_csv, DataFrame

df = read_csv('Carteira.csv')

df['Soma Ponderada (R$)'] = df['Quantidade'] * df['Compra (R$)']

conjunto = set(df['Ativo'])

ListaAtivos = []
ListaPrecoMedio = []

for nome in conjunto:

    ListaAtivos.append(nome)

    df2 = df.loc[ df['Ativo'] == nome ]

    SomaPesos = df2['Quantidade'].sum()

    SomaTotal = df2['Soma Ponderada (R$)'].sum()

    media = SomaTotal/SomaPesos

    ListaPrecoMedio.append(media)

dicionario = {'Ativo': ListaAtivos, 'Preço Médio de compra (R$)': ListaPrecoMedio}

df3 = DataFrame(dicionario)

df3.to_csv('PrecosMedios.csv', index = False)
