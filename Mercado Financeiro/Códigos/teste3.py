# Isso é só pra o terminal não colocar FutureWarnings quando o código é executado, mas é atualmente dispensável
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

from pandas import read_csv, to_datetime, DataFrame
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
# teste1 = []
# teste2 = []

caminho1 = '/home/gabriel/Github/gabrielnrt/Testes/'+'Mercado Financeiro'+'/Arquivos/'+'CarteiraGabriel.csv'
# carteira = read_csv('CarteiraGabriel.csv', delimiter='\t')
carteira = read_csv(caminho1, delimiter='\t')
carteira['Data da Aplicação'] = to_datetime(carteira['Data da Aplicação'], dayfirst=True)



ListaDeArquivos = ['ITSA4.SA.csv', 'SANB11.SA.csv', 'ITUB4.SA.csv', 'WEGE3.SA.csv']

figura, eixos = subplots(constrained_layout=True)
eixos.xaxis.set_major_locator(locator)
eixos.xaxis.set_major_formatter(formatter)

# Isso vai percorrer cada índice (linha), ou seja, k é um inteiro, k =0,1,2,...,n, onde n é o indice da ultima linha
for k in carteira.index:
    PrecoInicial = carteira.loc[k]['Preço de Compra']

    quantidade = carteira.loc[k]['Quantidade']

    # Isso vai servir de chave, só que para as datas
    DataComparativa = carteira.loc[k]['Data da Aplicação']

    acao = carteira.loc[k]['Renda Variável']
    chave = acao + '.SA.csv'

    for arquivo in ListaDeArquivos:
        if chave == arquivo:

            caminho2 = '/home/gabriel/Github/gabrielnrt/Testes/'+'Mercado Financeiro'+'/Arquivos/'+chave
            ativo = read_csv(caminho2, delimiter=',', usecols=['Date', 'Close'])
            ativo['Date'] = to_datetime(ativo['Date'], yearfirst=True)

            #(É AQUI QUE A SELEÇÃO DAS DATAS VAI ENTRAR)
            df = ativo[ativo.Date >= DataComparativa] # Isso cria um novo dataframe composto por datas maiores ou iguais a DataComparativa

            ValoresAbsolutos = []
            #ValoresPercentuais = []

            for k in df['Close']: # No fim desse for eu fico com uma lista pronta da variação
                preco = float(k)

                yAbsoluto = VariacaoAbsoluta(PrecoInicial,preco,quantidade)
                #yPercentual = VariacaoPercentual(PrecoInicial, preco)

                ValoresAbsolutos.append(yAbsoluto)
                #ValoresPercentuais.append(yPercentual)

            # Depois de plotar os dados, eles somem da memoria pq na próxima iteração a lista e o ativo['Date'] são resetados
            eixos.plot(df['Date'],ValoresAbsolutos, label=acao)
            #eixos.plot(ativo['Date'], ValoresPercentuais, label=acao)


            # teste1.append(df['Date'])
            # teste2.append(ValoresAbsolutos)



LegendaAbsoluta()

# print(teste1)
#
# TESTE = DataFrame(columns=['Datas', 'Preços'])
#print(TESTE)
#######################################################################################################################

figura, eixos = subplots(constrained_layout=True)
eixos.xaxis.set_major_locator(locator)
eixos.xaxis.set_major_formatter(formatter)

# Isso vai percorrer cada índice (linha), ou seja, k é um inteiro, k =0,1,2,...,n, onde n é o indice da ultima linha
for k in carteira.index:
    PrecoInicial = carteira.loc[k]['Preço de Compra']

    quantidade = carteira.loc[k]['Quantidade']

    # Isso vai servir de chave, só que para as datas
    DataComparativa = carteira.loc[k]['Data da Aplicação']

    acao = carteira.loc[k]['Renda Variável']
    chave = acao + '.SA.csv'

    for arquivo in ListaDeArquivos:
        if chave == arquivo:

            caminho2 = '/home/gabriel/Github/gabrielnrt/Testes/'+'Mercado Financeiro'+'/Arquivos/'+chave
            ativo = read_csv(caminho2, delimiter=',', usecols=['Date', 'Close'])
            ativo['Date'] = to_datetime(ativo['Date'], yearfirst=True)

            #(É AQUI QUE A SELEÇÃO DAS DATAS VAI ENTRAR)
            df = ativo[ativo.Date >= DataComparativa] # Isso cria um novo dataframe composto por datas maiores ou iguais a DataComparativa

            #ValoresAbsolutos = []
            ValoresPercentuais = []

            for k in df['Close']: # No fim desse for eu fico com uma lista pronta da variação
                preco = float(k)

                #yAbsoluto = VariacaoAbsoluta(PrecoInicial,preco,quantidade)
                yPercentual = VariacaoPercentual(PrecoInicial, preco)

                #ValoresAbsolutos.append(yAbsoluto)
                ValoresPercentuais.append(yPercentual)

            # Depois de plotar os dados, eles somem da memoria pq na próxima iteração a lista e o ativo['Date'] são resetados
            #eixos.plot(df['Date'],ValoresAbsolutos, label=acao)
            eixos.plot(df['Date'], ValoresPercentuais, label=acao)


            # teste1.append(df['Date'])
            # teste2.append(ValoresAbsolutos)



LegendaPercentual()
