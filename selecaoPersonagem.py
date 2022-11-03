import sys
import pygame as pg
from configJogo import ConfigJogo

class telaSelecao:
    def __init__(self, tela):
        self.tela = tela
        self.encerrada = False

        self.largura_retangulo = 0.5*ConfigJogo.LARGURA_TELA
        self.altura_retangulo = 0.6*ConfigJogo.ALTURA_TELA
        
        self.posicaoX_retangulo = (ConfigJogo.LARGURA_TELA * 0.25) 
        self.posicaoY_retangulo = (ConfigJogo.ALTURA_TELA * 0.25)

        self.cor_retangulo = (121, 126, 133)

        self.foto1_tamanho = pg.image.load("C:\\Users\\CT Junior\\Documents\\Mateus\\PythonGame\\PythonGame\\sprites\\teste.jpg").convert()
        self.imagerect = self.foto1_tamanho.get_rect()


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
        self.opcao_personagens(self.tela)
        self.desenha_opcao()
        
        pg.display.flip()

    def desenha_titulo(self, tela):
        px = ConfigJogo.LARGURA_TELA // 2 - self.titulo.get_size()[0] // 2
        py = (0.2 * ConfigJogo.ALTURA_TELA // 2)
        tela.blit(self.titulo, (px, py))

    def opcao_personagens(self, tela):
        tela.blit(self.foto1_tamanho, self.imagerect)

    def desenha_opcao(self):
        pg.draw.rect(
            self.tela, 
            self.cor_retangulo,
            pg.Rect(self.posicaoX_retangulo, self.posicaoY_retangulo, self.largura_retangulo, self.altura_retangulo)
        )