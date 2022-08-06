#---------------------------------------------------------
# Importação das bibliotecas

from pandas import DataFrame, read_csv
from datetime import datetime, date
from pandas_datareader import data as web
from numpy import average

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

# Função que retorna uma lista que é a soma acumulada da lista de entrada

def Soma(subcarteira):
    lista_antiga = list(subcarteira['Quantidade'])

    lista_nova = []
    for indice in range(0, len(lista_antiga)):
        if indice == 0:
            lista_nova.append(lista_antiga[indice])
        else:
            lista_nova.append( lista_antiga[indice] + lista_nova[indice - 1] )

    return lista_nova

# Lista de médias ponderadas
# TESTAR ESSA FUNÇÃO

def Media(subcarteira):
    resultado = []

    valores = list(subcarteira['Compra (R$)'])
    pesos = list(subcarteira['Quantidade'])

    v_parcial = []
    p_parcial = []

    for indice in range(0, len(valores)): # poderia ser len(pesos) também
        v_parcial.append(valores[indice])
        p_parcial.append(pesos[indice])

        media = average(a = v_parcial,
                        weights = p_parcial)

        resultado.append(media)

    return resultado



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

     subcarteira = subcarteira.reset_index(drop = True, inplace = False)

     subcarteira['Q_k'] = Soma(subcarteira)

     subcarteira['X_k'] = Media(subcarteira)

     df = yahoo(nome,subcarteira)

     df.drop(columns = ['High', 'Low', 'Open', 'Volume', 'Adj Close'],
             inplace = True)

     print(historico)
