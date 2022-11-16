from pygame import Surface
import pygame as pg

from configJogo import ConfigJogo
from cronometroArena import Cronometro 

class EstadoJogo:
    def __init__(self):
        self.cronometro = Cronometro()
        self.resetar()

    def resetar(self):
        self.cronometro.reset()

    def fim_de_jogo(self):
        if (self.cronometro.tempo_passando() > ConfigJogo.DURACAO_PARTIDA):
            return True 
        else:
            return False 