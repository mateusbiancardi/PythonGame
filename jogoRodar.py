import pygame as pg
from telaInicial import Menu
from telaInicial import Config

class JogoArena():
    def __init__(self):
        pg.init()

        self.tela = pg.display.set_mode((
            Config.LARGURA_TELA, 
            Config.ALTURA_TELA
        ))

    def rodar(self):
        cena = Menu(self.tela)
        cena.rodar()