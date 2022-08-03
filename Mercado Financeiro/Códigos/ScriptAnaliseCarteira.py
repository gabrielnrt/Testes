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

    dec = input('Digite o caractere de decimal: ')

    carteira = read_csv(arquivo,
                        sep = separador,
                        decimal = dec)
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
            carteira = DataFrame({'Ativo':Ativos,
                                  'Quantidade':Quantidades,
                                  'Compra (R$)':Precos,
                                  'Data da Compra':Fechas})

print(carteira)
