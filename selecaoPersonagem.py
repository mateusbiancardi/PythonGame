import sys
import pygame as pg
from configJogo import ConfigJogo

class telaSelecao:
    def __init__(self, tela):
        self.tela = tela
        self.encerrada = False
        
        font_titulo = pg.font.SysFont(None, ConfigJogo.FONTE_TITULO)
        self.titulo = font_titulo.render(
            f'Selecione seu personagem', True, ConfigJogo.COR_TITULO)
        
    def rodar(self):
        while not self.encerrada:
            self.tratamento_eventos()
            self.desenha()
    
    def tratamento_eventos(self):
        pg.event.get()

        # evento de saida
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)
            
        if pg.key.get_pressed()[pg.K_SPACE]:
            self.encerrada = True
    
    def desenha(self):
        self.tela.fill((255, 255, 255))
        self.desenha_titulo(self.tela)
        pg.display.flip()

    def desenha_titulo(self, tela):
        px = ConfigJogo.LARGURA_TELA // 2 - self.titulo.get_size()[0] // 2
        py = (0.2 * ConfigJogo.ALTURA_TELA // 2)
        tela.blit(self.titulo, (px, py))
        
    def personagens(self):
        pass