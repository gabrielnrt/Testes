"""
FAZER UMA FUNÇÃO EMA QUE SEJA ESCALÁVEL.
"""

from numpy import exp
from datetime import datetime, date
import pandas as pd



def ema0(serie, tau):

    """
    ESSA FUNÇÃO TEM COMO OBJETIVO RETORNAR O
    EMA DADOS APENAS A SÉRIE DE RETORNOS E O TAU.

    #--------------------------------------------------------
    ATENÇÃO: ELA CONSIDERA QUE A SÉRIE TEMPORAL SEJA
             HOMOGÊNEA E QUE t_n - t_{n-1} = 2 (CONSTANTE)
    #--------------------------------------------------------


    ENTRADA:
            - serie (pd.Series): Série de retornos.
            - tau (float): janela de dias da média móvel

    SAÍDA:
            - ret (pd.Series): Série da média móvel exponencial.

    """

    delta = 2

    alpha = delta/tau

    mi = exp(-alpha)

    ret=[]

    ret.append(serie[0])

    for indice in serie.index:

        if indice==0:

            ret.append(serie[0])

        else:

            termo1 = ret[indice-1]

            termo2 = serie[indice]

            expressao = mi*termo1 + (1-mi)*termo2

            ret.append(expressao)

    return ret


"""
As funções abaixo foram tiradas do próprio pandas:

https://pandas.pydata.org/docs/reference/api/pandas.Series.ewm.html

Nela, é usado a aproximação exp(x)~1+x no cálculo do EMA.
"""

def ema1(serie, tau):

    """
    ESSA FUNÇÃO TEM COMO OBJETIVO RETORNAR O
    EMA DADOS APENAS A SÉRIE DE RETORNOS E O TAU.

    #--------------------------------------------------------
    ATENÇÃO: ELA CONSIDERA QUE A SÉRIE TEMPORAL SEJA
             HOMOGÊNEA E QUE t_n - t_{n-1} = 2 (CONSTANTE)
    #--------------------------------------------------------


    ENTRADA:
            - serie (pd.Series): Série de retornos.
            - tau (float): janela de dias da média móvel

    SAÍDA:
            - ret (pd.Series): Série da média móvel exponencial.

    """

    # Isso é uma subclasse ExponentialMovingWindow
    objeto = serie.ewm(
                        span=tau-1, # Tem que colocar assi pq, na documentação, o denominador é 1+span
                        adjust=False # Coloquei como False pro cálculo ser iterativo, como está no Dacorogna
                      )

    ret = objeto.mean()

    return ret


def ema2(serie, datas, tau):

    """
    NESSA JÁ SE CONSIDERA QUE A DISTÂNCIA DE UMA DATA E OUTRA NÃO É CONSTANTE.


    ENTRADA:
            - serie (pd.Series): Série de retornos.

            - datas (pd.Series): Série de datas.
                                 PRECISA SER MONOTONICAMENTE CRESCENTE E
                                 DO TIPO datetime64[ns].

            - tau (float): janela de dias da média móvel.

    SAÍDA:
            - ret (pd.Series): Série da média móvel exponencial.
    """

    # Isso é uma subclasse ExponentialMovingWindow
    objeto = serie.ewm(
                        span=tau-1, # Tem que colocar assi pq, na documentação, o denominador é 1+span
                        adjust=False, # Coloquei como False pro cálculo ser iterativo, como está no Dacorogna
                        times=datas
                      )

    ret = objeto.mean()

    return ret
