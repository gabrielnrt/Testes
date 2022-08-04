#---------------------------------------------------------
# Importação das bibliotecas

from pandas import DataFrame, read_csv
from datetime import datetime, date
from pandas_datareader import data as web


#-----------------------------------------------------------
# Contantes

hoje = date.today()

#-----------------------------------------------------------
# Conversor de datas

def conversor(fecha):
    return datetime.strptime(fecha, '%d/%m/%Y')


# Requisição API Yahoo

def yahoo(ativo,tabela):

    fechas = list( tabela['Data da Compra'] )

    PrimeiraCompra = list[0]

    cotacoes = web.DataReader(ativo + '.SA',
                              data_source = 'yahoo',
                              start = PrimeiraCompra,
                              end = hoje)

    return cotacoes

#-------------------------------------------------------
# Arquivos de entrada

# Ativos = []
# Quantidades = []
# Precos = []
# Fechas = []

char = input('Você possui uma carteira em .csv pronta? [s/n] ')

if char == 's':
    arquivo = input('Digite o nome do arquivo incluindo o .csv: ')

    separador = input('Digite o caractere que separa as colunas: ')

    dec = input('Digite o caractere de decimal: ')

    carteira = read_csv(arquivo,
                        sep = separador,
                        decimal = dec,
                        parse_dates = ['Data da Compra'],
                        date_parser = conversor)
else:
    Ativos = []
    Quantidades = []
    Precos = []
    Fechas = []

    lampada = True
    while lampada:
        Ativos.append(input('\nDigite o código do ativo: '))

        Quantidades.append(int(input('Digite a quantidade comprada: ')))

        Precos.append(float(input('Digite o preço de compra da unidade: ')))

        Fechas.append(input('Digite a data da compra no formato dd/mm/aaaa: '))

        char = input('\nGostaria de inserir mais uma compra na carteira? [s/n]: ')

        if char == 'n':
            lampada = False

            dicionario = {'Ativo':Ativos,
                          'Quantidade':Quantidades,
                          'Compra (R$)':Precos,
                          'Data da Compra':Fechas}

            carteira = DataFrame(dicionario,
                                 parse_dates = ['Data da Compra'],
                                 date_parser = conversor)

#-----------------------------------------------------------------------------------
# Processamento de dados

carteira.sort_values(by = 'Data da Compra',
                     inplace = True)

lista = list( set(carteira['Ativo']) )

lista.sort()

for nome in lista:

     subcarteira = carteira.loc[ carteira['Ativo'] == nome ]

     historico = yahoo(nome,subcarteira)

     print(historico)
