import pygame as pg
from telaInicial import Menu
from configJogo import ConfigJogo

class JogoArena():
    def __init__(self):
        pg.init()

        self.tela = pg.display.set_mode((
            ConfigJogo.LARGURA_TELA, 
            ConfigJogo.ALTURA_TELA
        ))

    def rodar(self):
        cena = Menu(self.tela)
        cena.rodar()