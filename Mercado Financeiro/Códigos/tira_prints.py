import pyautogui
import pyperclip


class Scroll:

    coordenadas_seta_cima = (9,6)

    coordenadas_seta_baixo = (9,60)

    def __init__(self):
        pass

    @classmethod
    def rolar_para_cima(classe):
        # (...)
        return None




class Dia:

    coordenadas_dia = (20,20)

    coordenadas_botao_voltar = (10,20)

    def __init__(self):
        pass


    @classmethod
    def retrocede_um_dia(classe):
        # (...)
        return None

    @classmethod
    def volta_pra_hj(classe):
        # (...)
        return None

    @classmethod
    def pega_dia(classe):

        """
        Criar aqui as variáveis:

        Dia.string,
        Dia.objeto_date

        """

        return None

class Ticker_bbg:

    coordenadas = (0,0)

    def __init__(self):
        pass


    @classmethod
    def coleta_nome(classe):

        pyautogui.click(classe.coordenadas)
        # (...) copia o texto (...)
        x = pyperclip.paste('')

        classe.nome = x

        return None

    @classmethod
    def insere_nome(classe, nome_ativo):
        # (...)
        return None
