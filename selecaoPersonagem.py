import sys
import pygame as pg
import os
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

        self.sprite1_tamanho = pg.image.load(os.path.join('sprites', 'Guerreiro.png'))
        self.imagerect = self.sprite1_tamanho.get_rect()
        
        self.sprite1_posicao = (self.posicaoX_retangulo+10, self.posicaoY_retangulo+10)
        self.sprite2_posicao = (self.posicaoX_retangulo+10, self.posicaoY_retangulo+125)
        self.sprite3_posicao = (self.posicaoX_retangulo+10, self.posicaoY_retangulo+250)
        self.sprite4_posicao = (self.posicaoX_retangulo+10, self.posicaoY_retangulo+375)

        self.persoSelecionado = 1
        self.persoConfirmado = False
        self.personagem1 = 0
        self.personagem2 = 0

        font_titulo = pg.font.SysFont(None, ConfigJogo.FONTE_TITULO)
        self.titulo = font_titulo.render(
            f'Selecione seu personagem', True, ConfigJogo.COR_TITULO)
        
    def rodar(self):
        while not self.encerrada:
            self.tratamento_eventos()
            self.desenha()
    
    def tratamento_eventos(self):
        events = pg.event.get()

        # evento de saida
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)
        
        

        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    if self.persoSelecionado == 4:
                        self.persoSelecionado = 1
                        
                    else:
                        self.persoSelecionado += 1

                if event.key == pg.K_UP:
                    if self.persoSelecionado == 1:
                        self.persoSelecionado = 4

                    else:
                        self.persoSelecionado -= 1
                
                if event.key == pg.K_SPACE:
                    if self.personagem1 == 0:
                        self.persoConfirmado == True
                        
                    elif self.personagem2 == 0:
                        self.persoConfirmado == True


    
    def desenha(self):
        self.tela.fill((255, 255, 255))
        self.desenha_titulo(self.tela)
        self.desenha_opcao()
        self.personagemConfirmado()
        self.selecionar_personagem(self.tela)
        
        pg.display.flip()

    def desenha_titulo(self, tela):
        px = ConfigJogo.LARGURA_TELA // 2 - self.titulo.get_size()[0] // 2
        py = (0.2 * ConfigJogo.ALTURA_TELA // 2)
        tela.blit(self.titulo, (px, py))


    def selecionar_personagem(self,tela):
        
        tela.blit(self.sprite1_tamanho, self.sprite1_posicao)
        tela.blit(self.sprite1_tamanho, self.sprite2_posicao)
        tela.blit(self.sprite1_tamanho, self.sprite3_posicao)
        tela.blit(self.sprite1_tamanho, self.sprite4_posicao)

        if self.persoSelecionado == 1:

            if self.personagem1 == 0:
                if self.persoConfirmado:
                    self.personagem1 = self.persoSelecionado
            
            elif self.personagem2 == 0:
                if self.persoConfirmado:
                    self.personagem2 = self.persoSelecionado

            pg.draw.rect(
                self.tela, 
                (0,0,0),
                pg.Rect(self.posicaoX_retangulo, self.posicaoY_retangulo, self.largura_retangulo, 110),
                5
            )

        elif self.persoSelecionado == 2:
            
            if self.personagem1 == 0:
                if self.persoConfirmado:
                    self.personagem1 = self.persoSelecionado
            
            elif self.personagem2 == 0:
                if self.persoConfirmado:
                    self.personagem2 = self.persoSelecionado

            pg.draw.rect(
                self.tela, 
                (0,0,0),
                pg.Rect(self.posicaoX_retangulo, self.posicaoY_retangulo+125, self.largura_retangulo, 110),
                5
            )     

        elif self.persoSelecionado == 3:
            
            if self.personagem1 == 0:
                if self.persoConfirmado:
                    self.personagem1 = self.persoSelecionado
            
            elif self.personagem2 == 0:
                if self.persoConfirmado:
                    self.personagem2 = self.persoSelecionado

            pg.draw.rect(
                self.tela, 
                (0,0,0),
                pg.Rect(self.posicaoX_retangulo, self.posicaoY_retangulo+250, self.largura_retangulo, 110),
                5
            )

        elif self.persoSelecionado == 4:
            
            if self.personagem1 == 0:
                if self.persoConfirmado:
                    self.personagem1 = self.persoSelecionado
            
            elif self.personagem2 == 0:
                if self.persoConfirmado:
                    self.personagem2 = self.persoSelecionado

            pg.draw.rect(
                self.tela, 
                (0,0,0),
                pg.Rect(self.posicaoX_retangulo, self.posicaoY_retangulo+375, self.largura_retangulo, 110),
                5
            )

    def personagemConfirmado(self):
        if self.personagem1 == 1:
            pg.draw.rect(
                self.tela, 
                (0, 0, 204),
                pg.Rect(self.posicaoX_retangulo, self.posicaoY_retangulo, self.largura_retangulo, 110),
                5
            )

        elif self.personagem1 == 2:
            pg.draw.rect(
                self.tela, 
                (0,0,204),
                pg.Rect(self.posicaoX_retangulo, self.posicaoY_retangulo+125, self.largura_retangulo, 110),
                5
            )

        elif self.personagem1 == 3:
            pg.draw.rect(
                self.tela, 
                (0,0,204),
                pg.Rect(self.posicaoX_retangulo, self.posicaoY_retangulo+250, self.largura_retangulo, 110),
                5
            )

        elif self.personagem1 == 4:
            pg.draw.rect(
                self.tela, 
                (0,0,204),
                pg.Rect(self.posicaoX_retangulo, self.posicaoY_retangulo+375, self.largura_retangulo, 110),
                5
            )


    def desenha_opcao(self):
        pg.draw.rect(
            self.tela, 
            self.cor_retangulo,
            pg.Rect(self.posicaoX_retangulo, self.posicaoY_retangulo, self.largura_retangulo, self.altura_retangulo)
        )