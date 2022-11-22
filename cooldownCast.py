from pygame import Surface
import pygame as pg

from configJogo import ConfigJogo
from cronometroArena import Cronometro 

class CooldownCast:
    def __init__(self):
        self.cronometro = Cronometro()
        self.resetar()

    def resetar(self):
        self.cronometro.reset()

    def diferenca(self):
        return self.cronometro.tempo_passando()
            