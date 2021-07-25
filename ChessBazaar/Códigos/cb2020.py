# Isso é só pra o terminal não colocar FutureWarnings quando o código é executado, mas é atualmente dispensável
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


from pandas import read_csv, to_datetime
from numpy import array, shape
from pylab import plot, show, figure, xlabel, ylabel, legend, grid, xticks, plot_date, title
from matplotlib.dates import date2num


df = read_csv('ChessBazaar2020.csv', delimiter='\t')

# ESSE COMANDO TRANSFORMA ESSA COLUNA DE STRINGS ('object') EM UMA DE DATAS ('datetime64')
df['Data'] = to_datetime(df['Data'], dayfirst=True)


#-----------------------------------------------------------------------------
# #ESSE É DE OUTRO JEITO MAS DA NA MESMA
# #print(df['Data'])
# x = date2num(df['Data'])
# #print(type(xdate[0]))
# figure()
# plot_date(x, df['Sinquefield'], fmt='-', xdate=True, ydate=False)
# xticks(rotation=30)
# show()
#-----------------------------------------------------------------------------



figure()

## JEITO ANALÓGICO DE PLOTAR OS GRÁFICOS:
#plot_date(df['Data'], df['Sinquefield'], fmt='-')
#plot_date(df['Data'], df['1972'], fmt='-')
# e por aí vai...

## JEITO AUTOMATIZADO DE PLOTAR OS GRÁFICOS:
for i in df.columns:
    if i != 'Data':
        plot_date(df['Data'], df[i], fmt='-', label=i)

# ESSE COMANDO RODA O QUE TÁ ESCRITO NO EIXO X (NESSE CASO, FOI 30 GRAUS)
xticks(rotation=30)

#-----------------------------------------------------------------------------
## ESSES COMANDOS SÃO PRA 'ENFEITAR' O GRÁFICO
xlabel('Data')
ylabel('Preço (USD)')
grid(True, linestyle='--')
legend()
title('Peças Chessbazaar \n2020')
#-----------------------------------------------------------------------------

show()

#-----------------------------------------------------------------------------
#print(df.columns) # ISSO VAI DAR NUMA LISTA DE STRINGS
#for i in df.columns:
#    print(i)
#print(type(i)) ## CADA UM DESSES i's É UM STRING
#print(df.columns[0]) ## ISSO RETORNA O STRING 'Data'

#for i in df.columns:
#    print(df[i]) # ISSO PRINTA TODAS AS COLUNAS, SÓ QUE UMA POR VEZ

#x = array(df['Data'])
#print(type(x)) # É UM ARRAY DE STRINGS

df2 = read_csv('Cupons2020.csv', delimiter='\t')
df2['Data'] = to_datetime(df2['Data'], dayfirst=True)

figure()
for i in df2.columns:
    if i != 'Data':
        plot_date(df2['Data'], df2[i], fmt='-', label=i)

xticks(rotation=30)
xlabel('Data')
grid(True, linestyle='--')
legend()
title('Cupons de desconto Chessbazaar \n2020')

show()
