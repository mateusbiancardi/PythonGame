import pygame as pg
import sys
import os
from configJogo import ConfigJogo
from selecaoPersonagem import telaSelecao
from personagens import Personagem

class telaPrincipal():
    def __init__(self, tela, escolhidos):
        self.tela = tela
        self.encerrada = False
        
        
        p1 = Personagem(escolhidos[0], self.tela)
        p2 = Personagem(escolhidos[1], self.tela)
        
        p1.stats()
        p2.stats()
        
        self.p1AtaqueE = False
        
        self.p1Velocidade = p1.status[0]
        self.p2Velocidade = p2.status[0]
        
        self.p1Vida = p1.status[1]
        self.p2Vida = p2.status[1]
        self.p1VidaTotal = p1.status[1]
        self.p2VidaTotal = p2.status[1]
        
        self.p1 = p1.status[2]
        self.p2 = p2.status[2]
        
        self.p1VelocidadeAtq = p1.status[3]
        self.p2VelocidadeAtq = p2.status[3]
        
        self.p1Dano = p1.status[4]
        self.p2Dano = p2.status[4]
        
        
        self.xP1 = ConfigJogo.LARGURA_TELA * (1/3)
        self.yP1 = ConfigJogo.ALTURA_TELA // 2
        self.v_xP1 = 0
        self.v_yP1 = 0
        
        self.xP2 = ConfigJogo.LARGURA_TELA * (2/3)
        self.yP2 = ConfigJogo.ALTURA_TELA // 2
        self.v_xP2 = 0
        self.v_yP2 = 0
    
        self.sprite1_tamanho = pg.image.load(os.path.join('sprites', 'guerreiro.png'))
        self.sprite2_tamanho = pg.image.load(os.path.join('sprites', 'mago.png'))
        self.sprite3_tamanho = pg.image.load(os.path.join('sprites', 'xama.png'))
        self.sprite4_tamanho = pg.image.load(os.path.join('sprites', 'arqueiro.png'))
        
        self.imagerect = self.sprite1_tamanho.get_rect()
        
        
        self.raioATQGiratorio = 50
        
        
    def rodar(self):
        while not self.encerrada:
            self.tela.fill((102, 255, 51))
            self.carregarPersonagem()
            self.tratamentoEventos()
            self.movimento()
            self.ataques()
            self.personagem()
            
            pg.display.flip()
            
    def tratamentoEventos(self):
        events = pg.event.get()
            
        for event in events:
            #Personagem 1 (W A S D)
            
            if ((event.type == pg.KEYDOWN) and (event.key == pg.K_a)) or (pg.key.get_pressed()[pg.K_a]):
                self.v_xP1 = -self.p1Velocidade

            if ((event.type == pg.KEYDOWN) and (event.key == pg.K_d)) or (pg.key.get_pressed()[pg.K_d]):
                self.v_xP1 = self.p1Velocidade
                
            if ((event.type == pg.KEYDOWN) and (event.key == pg.K_w)) or (pg.key.get_pressed()[pg.K_w]):
                self.v_yP1 = -self.p1Velocidade

            if ((event.type == pg.KEYDOWN) and (event.key == pg.K_s)) or (pg.key.get_pressed()[pg.K_s]):
                self.v_yP1 = self.p1Velocidade
                
            if ((event.type == pg.KEYUP) and (event.key == pg.K_a)) or \
                        ((event.type == pg.KEYUP) and (event.key == pg.K_d)):
                self.v_xP1 = 0
                
            
                
            if ((event.type == pg.KEYUP) and (event.key == pg.K_w)) or \
                        ((event.type == pg.KEYUP) and (event.key == pg.K_s)):
                self.v_yP1 = 0
                
                
            if ((event.type == pg.KEYDOWN) and (event.key == pg.K_e)) or (pg.key.get_pressed()[pg.K_e]):
                self.p1AtaqueE = True
                
            
            #Personagem 2 (setinhas)
            if ((event.type == pg.KEYDOWN) and (event.key == pg.K_LEFT)) or (pg.key.get_pressed()[pg.K_LEFT]):
                self.v_xP2 = -self.p2Velocidade

            if ((event.type == pg.KEYDOWN) and (event.key == pg.K_RIGHT)) or (pg.key.get_pressed()[pg.K_RIGHT]):
                self.v_xP2 = self.p2Velocidade
                
            if ((event.type == pg.KEYDOWN) and (event.key == pg.K_UP)) or (pg.key.get_pressed()[pg.K_UP]):
                self.v_yP2 = -self.p2Velocidade

            if ((event.type == pg.KEYDOWN) and (event.key == pg.K_DOWN)) or (pg.key.get_pressed()[pg.K_DOWN]):
                self.v_yP2 = self.p2Velocidade
                
            if ((event.type == pg.KEYUP) and (event.key == pg.K_LEFT)) or \
                        ((event.type == pg.KEYUP) and (event.key == pg.K_RIGHT)):
                self.v_xP2 = 0
                
            if ((event.type == pg.KEYUP) and (event.key == pg.K_UP)) or \
                        ((event.type == pg.KEYUP) and (event.key == pg.K_DOWN)):
                self.v_yP2 = 0
                
        # evento de saida
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)
    
    def movimento(self):
        
        if (self.xP1 + self.v_xP1 < 0) or (self.xP1 + self.v_xP1 > ConfigJogo.LARGURA_TELA-50):
            self.v_xP1 = 0
        if (self.yP1 + self.v_yP1 < 0) or (self.yP1 + self.v_yP1 > ConfigJogo.ALTURA_TELA-50):
            self.v_yP1 = 0
            
        if (self.xP2 + self.v_xP2 < 0) or (self.xP2 + self.v_xP2 > ConfigJogo.LARGURA_TELA-50):
            self.v_xP2 = 0
        if (self.yP2 + self.v_yP2 < 0) or (self.yP2 + self.v_yP2 > ConfigJogo.ALTURA_TELA-50):
            self.v_yP2 = 0
        
        self.xP1 += self.v_xP1
        self.yP1 += self.v_yP1
            
        self.xP2 += self.v_xP2
        self.yP2 += self.v_yP2
        
    def carregarPersonagem(self):
        if self.p1 == 1:
            self.sprite1_tamanho = pg.image.load(os.path.join('sprites', 'guerreiro.png'))
            
        elif self.p1 == 2:
            self.sprite1_tamanho = pg.image.load(os.path.join('sprites', 'mago.png'))
            
        elif self.p1 == 3:
            self.sprite1_tamanho = pg.image.load(os.path.join('sprites', 'xama.png'))
            
        elif self.p1 == 4:
            self.sprite1_tamanho = pg.image.load(os.path.join('sprites', 'arqueiro.png'))
            
            
            
        if self.p2 == 1:
            self.sprite2_tamanho = pg.image.load(os.path.join('sprites', 'guerreiro.png'))
            
        elif self.p2 == 2:
            self.sprite2_tamanho = pg.image.load(os.path.join('sprites', 'mago.png'))
            
        elif self.p2 == 3:
            self.sprite2_tamanho = pg.image.load(os.path.join('sprites', 'xama.png'))
            
        elif self.p2 == 4:
            self.sprite2_tamanho = pg.image.load(os.path.join('sprites', 'arqueiro.png'))
            
    
    def personagem (self):
        
        font_vida = pg.font.SysFont(None, ConfigJogo.FONTE_VIDA)
        self.textoVida1 = font_vida.render(
            f'{self.p1Vida}/{self.p1VidaTotal}', True, ConfigJogo.COR_VIDA)
        
        self.textoVida2 = font_vida.render(
            f'{self.p2Vida}/{self.p2VidaTotal}', True, ConfigJogo.COR_VIDA)
        
        self.tela.blit(self.textoVida1, (self.xP1, self.yP1-20))
        self.tela.blit(self.textoVida2, (self.xP2, self.yP2-20))
        
        self.tela.blit(self.sprite1_tamanho, (self.xP1, self.yP1))
        self.tela.blit(self.sprite2_tamanho, (self.xP2, self.yP2)) 
        
    def ataques(self):
        self.xP1CirculoCentralizado = self.xP1+30
        self.yP1CirculoCentralizado = self.yP1+25
        
        
        #Ataque Giratório Guerreiro P1
        if self.p1 == 1 and self.p1AtaqueE:
            pg.draw.circle(self.tela, (0,0,0), (self.xP1CirculoCentralizado, self.yP1CirculoCentralizado), self.raioATQGiratorio, 5)
            
            #Se o p2 está localizado na área de p1:
            if (int(self.xP2) in range (int(self.xP1CirculoCentralizado-self.raioATQGiratorio), int(self.xP1CirculoCentralizado+self.raioATQGiratorio)) or \
                int (self.xP2+40) in range (int(self.xP1CirculoCentralizado-self.raioATQGiratorio), int(self.xP1CirculoCentralizado+self.raioATQGiratorio))) and \
                    (int(self.yP2) in range (int(self.yP1CirculoCentralizado-self.raioATQGiratorio), int(self.yP1CirculoCentralizado+self.raioATQGiratorio)) or \
                        int(self.yP2+55) in range (int(self.yP1CirculoCentralizado-self.raioATQGiratorio), int(self.yP1CirculoCentralizado+self.raioATQGiratorio))):
                        self.p2Vida = self.p2Vida-self.p1Dano