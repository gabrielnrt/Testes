# O jeito antigo ta em cb2020.py

# Isso é só pra o terminal não colocar FutureWarnings quando o código é executado, mas é atualmente dispensável
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

from pandas import read_csv, to_datetime
from numpy import array, shape
from pylab import plot, show, figure, xlabel, ylabel, legend, grid, xticks, plot_date, title, subplots
from matplotlib.dates import AutoDateLocator, ConciseDateFormatter

# Primeiro grafico:

df = read_csv('ChessBazaar2021.csv', delimiter='\t')

# ESSE COMANDO TRANSFORMA ESSA COLUNA DE STRINGS ('object') EM UMA DE DATAS ('datetime64')
df['Data'] = to_datetime(df['Data'], dayfirst=True)

figura, eixos = subplots(constrained_layout=True)

#-----------------------------------------------------------------------------
# Eu até agora não sei o que esses comandos fazem exatamente,
# mas são eles que fazem o eixo x ficar melhor organizado
locator = AutoDateLocator()
formatter = ConciseDateFormatter(locator)
eixos.xaxis.set_major_locator(locator)
eixos.xaxis.set_major_formatter(formatter)
#-----------------------------------------------------------------------------

for i in df.columns:
    if i != 'Data':
        eixos.plot(df['Data'],df[i], label=i)


legend()
grid(True, linestyle='--')
xlabel('Data')
ylabel('Preço (USD)')
title('Peças Chessbazaar \n2021')

# # ESSE COMANDO RODA O QUE TÁ ESCRITO NO EIXO X (NESSE CASO, FOI 30 GRAUS)
# xticks(rotation=30)

show()

###############################################################################
# Segundo grafico:

df2 = read_csv('Cupons2021.csv', delimiter='\t')
df2['Data'] = to_datetime(df2['Data'], dayfirst=True)

fig, ax = subplots(constrained_layout=True)

ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

ax.plot(df2['Data'],df2['Valor do desconto'])

grid(True, linestyle='--')
xlabel('Data')
ylabel('Desconto (%)')
title('Cupons de desconto Chessbazaar \n2021')

show()
