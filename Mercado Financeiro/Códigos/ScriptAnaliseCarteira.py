#---------------------------------------------------------
# Importação das bibliotecas

from pandas import DataFrame, read_csv

#-------------------------------------------------------
# Arquivos de entrada

Ativos = []
Quantidades = []
Precos = []
Fechas = []

char = input('Você possui uma carteira em .csv pronta? [s/n] ')

if char == 's':
    arquivo = input('Digite o nome do arquivo incluindo o .csv: ')
    separador = input('Digite o caractere que separa as colunas: ')
    carteira = read_csv(arquivo, sep = separador)
else:
    Ativos = []
    Quantidades = []
    Precos = []
    Fechas = []

    lampada = True
    while lampada:
        Ativos.append(input('Digite o código do ativo: '))

        Quantidades.append(int(input('Digite a quantidade comprada: ')))

        Precos.append(float(input('Digite o preço de compra da unidade: ')))

        Fechas.append(input('Digite a data da compra no formato dd/mm/aaaa: '))

        char = input('Gostaria de inserir mais uma compra na carteira? [s/n]: ')

        if char == 'n':
            lampada = False
