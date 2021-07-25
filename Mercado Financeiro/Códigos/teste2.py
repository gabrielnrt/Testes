# Isso é só pra o terminal não colocar FutureWarnings quando o código é executado, mas é atualmente dispensável
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

from pandas import read_csv, to_datetime
from numpy import array, shape
from pylab import plot, show, figure, xlabel, ylabel, legend, grid, xticks, plot_date, title, subplots
from matplotlib.dates import AutoDateLocator, ConciseDateFormatter


locator = AutoDateLocator()
formatter = ConciseDateFormatter(locator)


def VariacaoAbsoluta(incicio, fim, quantidade):
    x = (fim - incicio)*quantidade
    return x

def VariacaoPercentual(inicio, fim):
    x = (fim - inicio)/inicio
    return x

def LegendaAbsoluta():
    legend()
    grid(True, linestyle='--')
    xlabel('Data')

    ylabel('R$')
    title('Variação Absoluta')
    show()

def LegendaPercentual():
    legend()
    grid(True, linestyle='--')
    xlabel('Data')

    ylabel('%')
    title('Variação Percentual')
    show()


######################################################################################################################

carteira = read_csv('CarteiraGabriel.csv', delimiter='\t')
carteira['Data da Aplicação'] = to_datetime(carteira['Data da Aplicação'], dayfirst=True)



ListaDeArquivos = ['ITSA4.SA.csv', 'SANB11.SA.csv']

figura, eixos = subplots(constrained_layout=True)
eixos.xaxis.set_major_locator(locator)
eixos.xaxis.set_major_formatter(formatter)

# Isso vai percorrer cada índice (linha), ou seja, k é um inteiro, k =0,1,2,...,n, onde n é o indice da ultima linha
for k in carteira.index:
    PrecoInicial = carteira.loc[k]['Preço de Compra']

    quantidade = carteira.loc[k]['Quantidade']

    acao = carteira.loc[k]['Renda Variável']
    chave = acao + '.SA.csv'

    for arquivo in ListaDeArquivos:
        if chave == arquivo:
            ativo = read_csv(arquivo, delimiter=',', usecols=['Date', 'Close'])
            ativo['Date'] = to_datetime(ativo['Date'], yearfirst=True)

            ValoresAbsolutos = []
            #ValoresPercentuais = []

            for k in ativo['Close']:
                preco = float(k)

                yAbsoluto = VariacaoAbsoluta(PrecoInicial,preco,quantidade)
                #yPercentual = VariacaoPercentual(PrecoInicial, preco)

                ValoresAbsolutos.append(yAbsoluto)
                #ValoresPercentuais.append(yPercentual)


            eixos.plot(ativo['Date'],ValoresAbsolutos, label=acao)
            #eixos.plot(ativo['Date'], ValoresPercentuais, label=acao)

LegendaAbsoluta()

#------------------------------------------------------------------------------------------------------------------------

figura, eixos = subplots(constrained_layout=True)
eixos.xaxis.set_major_locator(locator)
eixos.xaxis.set_major_formatter(formatter)

# Isso vai percorrer cada índice (linha), ou seja, k é um inteiro, k =0,1,2,...,n, onde n é o indice da ultima linha
for k in carteira.index:
    PrecoInicial = carteira.loc[k]['Preço de Compra']

    quantidade = carteira.loc[k]['Quantidade']

    acao = carteira.loc[k]['Renda Variável']
    chave = acao + '.SA.csv'

    for arquivo in ListaDeArquivos:
        if chave == arquivo:
            ativo = read_csv(arquivo, delimiter=',', usecols=['Date', 'Close'])
            ativo['Date'] = to_datetime(ativo['Date'], yearfirst=True)

            #ValoresAbsolutos = []
            ValoresPercentuais = []

            for k in ativo['Close']:
                preco = float(k)

                #yAbsoluto = VariacaoAbsoluta(PrecoInicial,preco,quantidade)
                yPercentual = VariacaoPercentual(PrecoInicial, preco)

                #ValoresAbsolutos.append(yAbsoluto)
                ValoresPercentuais.append(yPercentual)


            #eixos.plot(ativo['Date'],ValoresAbsolutos, label=acao)
            eixos.plot(ativo['Date'], ValoresPercentuais, label=acao)

LegendaPercentual()
