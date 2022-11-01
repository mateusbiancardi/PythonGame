import math
import random
import sys
import pygame as pg
from time import time

class Config:
    LARGURA_TELA = 600
    ALTURA_TELA = 400
    FONTE_TITULO = 72
    FONTE_SUBTITULO = 24
    COR_FUNDO = (0, 0, 255)
    COR_TITULO = (0, 0, 0)

class Cronometro:
    def __init__(self):
        self.reset()

    def reset(self):
        self.tempo_referencia = time()

    def tempo_passando(self):
        tempo_atual = time()
        return tempo_atual - self.tempo_referencia

class Menu:
    def __init__(self, tela):
        self.tela = tela 
        self.encerrada = False

        font_titulo = pg.font.SysFont(None, Config.FONTE_TITULO)
        font_subtitulo = pg.font.SysFont(None, Config.FONTE_SUBTITULO)
        self.titulo = font_titulo.render(
            f'Jogo de Arena', True, Config.COR_TITULO)
        self.subtitulo = font_subtitulo.render(
            f'Pressione espaço para iniciar', True, Config.COR_TITULO)

        self.cronometro = Cronometro()
        self.mostrar_subtitulo = True

    def rodar(self):
        while not self.encerrada:
            self.eventos()
            self.atualiza_estado()
            self.desenha()

    def eventos(self):
        pg.event.get()
        
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)

        if pg.key.get_pressed()[pg.K_SPACE]:
            self.encerrada = True

    def atualiza_estado(self):
        if self.cronometro.tempo_passando() > 0.5:
            self.mostrar_subtitulo = not self.mostrar_subtitulo
            self.cronometro.reset()

    def desenha(self):
        self.tela.fill((255, 255, 255))
        self.desenha_titulo(self.tela)
        self.desenha_subtitulo(self.tela)
        pg.display.flip()

    def desenha_titulo(self, tela):
        px = Config.LARGURA_TELA // 2 - self.titulo.get_size()[0] // 2
        py = (0.2 * Config.ALTURA_TELA // 2)
        tela.blit(self.titulo, (px, py))

    def desenha_subtitulo(self, tela):
        if self.mostrar_subtitulo:
            px = Config.LARGURA_TELA // 2 - \
                self.subtitulo.get_size()[0] // 2
            py = (0.2 * Config.ALTURA_TELA // 2) + \
                (self.titulo.get_size()[1] * 1.5)
            tela.blit(self.subtitulo, (px, py))

class JogoArena:
    def __init__(self):
        pg.init()

        self.tela = pg.display.set_mode((
            Config.LARGURA_TELA, 
            Config.ALTURA_TELA
        ))

    def rodar(self):
        cena = Menu(self.tela)
        cena.rodar()