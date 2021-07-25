# Isso é só pra o terminal não colocar FutureWarnings quando o código é executado, mas é atualmente dispensável
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

from pandas import read_csv, to_datetime, DataFrame
from numpy import array, shape
from pylab import plot, show, figure, xlabel, ylabel, legend, grid, xticks, plot_date, title, subplots
from matplotlib.dates import AutoDateLocator, ConciseDateFormatter

# Fazer um programa que retorna o grafico com a variação percentual dos ativos que estão numa lista dada, como ['AZUL4.SA.csv','GOLL4.csv']
# essa lista é colocada na mão

locator = AutoDateLocator()
formatter = ConciseDateFormatter(locator)

def VariacaoPercentual(inicio, fim):
    x = (fim - inicio)/inicio
    return x

# def grafico(x,y):
# #def grafico(x,y, legenda):
#     # Aqui eu to assumindo que x é um conjunto de datas
#
#     figura, eixos = subplots(constrained_layout=True)
#     eixos.xaxis.set_major_locator(locator)
#     eixos.xaxis.set_major_formatter(formatter)
#
#     # eixos.plot(x,y, label=legenda)
#     eixos.plot(x,y)
#
#     #legend()
#     grid(True, linestyle='--')
#     xlabel('Data')
#     ylabel('%')
#     title('Variação Percentual')
#
#     show()

def grafico(lista):

    figura, eixos = subplots(constrained_layout=True)
    eixos.xaxis.set_major_locator(locator)
    eixos.xaxis.set_major_formatter(formatter)

    for acao in lista:

        arquivo = acao + '.SA.csv'

        # OBS: o parâmetro parse_dates é útil quando as datas estão no formato 'Ano-Mês-Dia'.
        ## Com outros formatos ele pode não funcionar direito.
        ## Na dúvida, é só usar depois a função to_datetime
        df = read_csv(arquivo, delimiter = ',', usecols = ['Date', 'Close'], parse_dates = ['Date'])

        PrecoInicial = df.loc[0]['Close']

        datas = df['Date']
        variacoes = []

        for preco in df['Close']:

            PrecoFinal = float(preco)
            variacao = VariacaoPercentual(PrecoInicial,PrecoFinal)
            variacoes.append(variacao)

        eixos.plot(datas, variacoes, label = acao)


    legend()
    grid(True, linestyle='--')
    xlabel('Data')
    ylabel('%')
    title('Variação Percentual')

    show()


LISTA = ['AZUL4', 'GOLL4', 'CVCB3', 'EMBR3']

grafico(LISTA)
