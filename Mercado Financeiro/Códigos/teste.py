# Isso é só pra o terminal não colocar FutureWarnings quando o código é executado, mas é atualmente dispensável
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

from pandas import read_csv, to_datetime
from numpy import array, shape
from pylab import plot, show, figure, xlabel, ylabel, legend, grid, xticks, plot_date, title, subplots
from matplotlib.dates import AutoDateLocator, ConciseDateFormatter

def VariacaoAbsoluta(incicio, fim, quantidade):
    x = (fim - incicio)*quantidade
    return x

def VariacaoPercentual(inicio, fim):
    x = (fim - inicio)/inicio
    return x

def grafico(x,y):
    figura, eixos = subplots(constrained_layout=True)

    locator = AutoDateLocator()
    formatter = ConciseDateFormatter(locator)
    eixos.xaxis.set_major_locator(locator)
    eixos.xaxis.set_major_formatter(formatter)

    eixos.plot(x,y, label='ITSA4')

    legend()
    grid(True, linestyle='--')
    xlabel('Data')


def LegendaAbsoluta():
    ylabel('R$')
    title('Variação Absoluta')
    show()

def LegendaPercentual():
    ylabel('%')
    title('Variação Percentual')
    show()

######################################################################################################################

# Indo pra n-ésima linha: df.loc[n]
# Pra selecionar o elemento de uma determinada coluna da n-ésima linha, é só fazer df.loc[n].['Nome da coluna']

# Indo para a última linha: df.tail(1)
# Pra selecionar o elemento de uma determinada coluna da última linha, é só fazer df.tail(1).['Nome da coluna']


carteira = read_csv('CarteiraGabriel.csv', delimiter='\t')
#carteira['Data'] = to_datetime(carteira['Data'], dayfirst=True)

# # Essa linha vai ter que ser generalizada dps pra algo como
# for x in carteira['Preço de Compra']:
#     PrecoInicial = float(x)
PrecoInicial = float(carteira.loc[0]['Preço de Compra'])

quantidade = int( carteira.loc[0]['Quantidade'] )

#---------------------------------------------------------------------------------------------------------------------

ativo = read_csv('ITSA4.SA.csv', delimiter=',', usecols=['Date', 'Close'])

# PrecoFinal = float(ativo.tail(1)['Close'])
#
# VA = VariacaoAbsoluta(PrecoInicial, PrecoFinal, quantidade)
# VP = VariacaoPercentual(PrecoInicial, PrecoFinal)
#
# print('Ativo:'+'ITSA4')
# print('Variação Absoluta:', VA)
# print('Variação Percentual:', VP)


#####################################################################################################################
ativo['Date'] = to_datetime(ativo['Date'], yearfirst=True)

ValoresAbsolutos = []
ValoresPercentuais = []

for k in ativo['Close']:
    preco = float(k)
    yAbsoluto = VariacaoAbsoluta(PrecoInicial,preco,quantidade)
    yPercentual = VariacaoPercentual(PrecoInicial, preco)

    ValoresAbsolutos.append(yAbsoluto)
    ValoresPercentuais.append(yPercentual)



# figura, eixos = subplots(1,2, constrained_layout=True)
#
# locator = AutoDateLocator()
# formatter = ConciseDateFormatter(locator)
#
# eixos.xaxis.set_major_locator(locator)
# eixos.xaxis.set_major_formatter(formatter)
#
# eixos.plot(ativo['Date'], ValoresAbsolutos, label='ITSA4')
# eixos.plot(ativo['Date'], ValoresPercentuais)
#
# legend()
# grid(True, linestyle='--')
# xlabel('Data')
# show()

grafico(ativo['Date'],ValoresAbsolutos)
LegendaAbsoluta()

grafico(ativo['Date'], ValoresPercentuais)
LegendaPercentual()
