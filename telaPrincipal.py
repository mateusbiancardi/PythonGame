import pygame as pg
import sys
import os
from configJogo import ConfigJogo
from selecaoPersonagem import telaSelecao
from personagens import Personagem
from cooldownCast import CooldownCast
from time import time

class telaPrincipal():
    def __init__(self, tela, escolhidos):
        self.tela = tela
        self.encerrada = False
        self.primeiroCastE = True
        self.primeiroCastQ = True
        self.primeiroCastM = True
        self.primeiroCastN = True
        
        p1 = Personagem(escolhidos[0], self.tela)
        p2 = Personagem(escolhidos[1], self.tela)
        
        self.CastE = CooldownCast()
        self.CastQ = CooldownCast()
        
        self.CastM = CooldownCast()
        self.CastN = CooldownCast()
        
        p1.stats()
        p2.stats()
        
        self.p1AtaqueE = False
        self.p1AtaqueQ = False
        
        self.p2AtaqueM = False
        self.p2AtaqueN = False
        
        self.p1Velocidade = p1.status[0]
        self.p2Velocidade = p2.status[0]
        self.p1VelocidadePadrao = p1.status[0]
        self.p2VelocidadePadrao = p2.status[0]
        
        self.p1Vida = p1.status[1]
        self.p2Vida = p2.status[1]
        self.p1VidaAntes = p1.status[1]
        self.p2VidaAntes = p2.status[1]
        self.p1VidaTotal = p1.status[1]
        self.p2VidaTotal = p2.status[1]
        
        self.p1 = p1.status[2]
        self.p2 = p2.status[2]
        
        self.p1VelocidadeAtq = p1.status[3]
        self.p2VelocidadeAtq = p2.status[3]
        
        self.p1Dano = p1.status[4]
        self.p2Dano = p2.status[4]
        self.p1DanoPadrao = p1.status[4]
        self.p2DanoPadrao = p2.status[4]
        
        
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
        
        self.raioATQProjetil = 150
        
    def rodar(self):
        while not self.encerrada:
            self.tela.fill((102, 255, 51))
            self.tratamentoEventos()
            self.movimento()
            self.ataques()
            self.carregarPersonagem()
            
            pg.display.flip()
            
    def tratamentoEventos(self):
        events = pg.event.get()
            
        for event in events:
            #Personagem 1 (W A S D)
            #Movimentação
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
                   
            #Ataque E
            if ((event.type == pg.KEYDOWN) and (event.key == pg.K_e)) or (pg.key.get_pressed()[pg.K_e]):
                cooldownCastE = self.CastE.diferenca()
                
                if (cooldownCastE > self.p1VelocidadeAtq) or self.primeiroCastE:
                    self.p1AtaqueE = True
                    self.CastE.resetar()
                    self.duracaoCastE = time()
                    self.primeiroCastE = False
                    
            
            #Ataque Q
            if ((event.type == pg.KEYDOWN) and (event.key == pg.K_q)) or (pg.key.get_pressed()[pg.K_q]):
                cooldownCastQ = self.CastQ.diferenca()
                
                if (cooldownCastQ > self.p1VelocidadeAtq*3) or self.primeiroCastQ:
                    self.p1AtaqueQ = True
                    self.CastQ.resetar()
                    self.duracaoCastQ = time()
                    self.primeiroCastQ = False
            
            #Personagem 2 (setinhas)
            #Movimentação
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
                
                
            #Ataque M
            if ((event.type == pg.KEYDOWN) and (event.key == pg.K_m)) or (pg.key.get_pressed()[pg.K_m]):
                cooldownCastM = self.CastM.diferenca()
                
                if (cooldownCastM > self.p2VelocidadeAtq) or self.primeiroCastM:
                    self.p2AtaqueM = True
                    self.CastM.resetar()
                    self.duracaoCastM = time()
                    self.primeiroCastM = False
            
            #Ataque N
            if ((event.type == pg.KEYDOWN) and (event.key == pg.K_n)) or (pg.key.get_pressed()[pg.K_n]):
                cooldownCastN = self.CastN.diferenca()
                
                if (cooldownCastN > self.p2VelocidadeAtq*3) or self.primeiroCastN:
                    self.p2AtaqueN = True
                    self.CastN.resetar()
                    self.duracaoCastN = time()
                    self.primeiroCastN = False
           
                
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
            
        self.personagem()
            
    
    def personagem (self):
        
        self.berserker = pg.image.load(os.path.join('sprites', 'berserker.png'))
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
        
        self.xP2CirculoCentralizado = self.xP2+30
        self.yP2CirculoCentralizado = self.yP2+25
        
        #Jogador 1
        #Guerreiro
        #Ataque Giratório (Q)
        if self.p1 == 1 and self.p1AtaqueE:
            if time() - self.duracaoCastE < 0.1:
                pg.draw.circle(self.tela, (0,0,0), (self.xP1CirculoCentralizado, self.yP1CirculoCentralizado), self.raioATQGiratorio, 5)
                #Se o p2 está localizado na área de p1:
                if ((int(self.xP2) in range (int(self.xP1CirculoCentralizado-self.raioATQGiratorio), int(self.xP1CirculoCentralizado+self.raioATQGiratorio)) or \
                    int (self.xP2+40) in range (int(self.xP1CirculoCentralizado-self.raioATQGiratorio), int(self.xP1CirculoCentralizado+self.raioATQGiratorio))) and \
                        (int(self.yP2) in range (int(self.yP1CirculoCentralizado-self.raioATQGiratorio), int(self.yP1CirculoCentralizado+self.raioATQGiratorio)) or \
                            int(self.yP2+55) in range (int(self.yP1CirculoCentralizado-self.raioATQGiratorio), int(self.yP1CirculoCentralizado+self.raioATQGiratorio)))) and \
                                self.p2Vida - self.p2VidaAntes == 0:
                                    self.p2Vida = self.p2Vida-self.p1Dano
            else:
                self.p2VidaAntes = self.p2Vida
        
        #Berserk - Aumenta o dano e velocidade de ataque por um breve momento(E)   
        if self.p1 == 1 and self.p1AtaqueQ:
            if time() - self.duracaoCastQ < 3:
                self.tela.blit(self.berserker, (self.xP1+10, self.yP1-50))
                self.p1Velocidade = 0.5
                self.p1Dano = 10
            else:
                self.p1Velocidade = self.p1VelocidadePadrao
                self.p1Dano = self.p1DanoPadrao
                
          
        #Jogador 2
        #Guerreiro
        #Ataque Giratório (Q)        
        if self.p2 == 1 and self.p2AtaqueM:
            if time() - self.duracaoCastM < 0.1:
                pg.draw.circle(self.tela, (0,0,0), (self.xP2CirculoCentralizado, self.yP2CirculoCentralizado), self.raioATQGiratorio, 5)
                #Se o p1 está localizado na área de p2:
                if ((int(self.xP1) in range (int(self.xP2CirculoCentralizado-self.raioATQGiratorio), int(self.xP2CirculoCentralizado+self.raioATQGiratorio)) or \
                    int (self.xP1+40) in range (int(self.xP2CirculoCentralizado-self.raioATQGiratorio), int(self.xP2CirculoCentralizado+self.raioATQGiratorio))) and \
                        (int(self.yP1) in range (int(self.yP2CirculoCentralizado-self.raioATQGiratorio), int(self.yP2CirculoCentralizado+self.raioATQGiratorio)) or \
                            int(self.yP1+55) in range (int(self.yP2CirculoCentralizado-self.raioATQGiratorio), int(self.yP2CirculoCentralizado+self.raioATQGiratorio)))) and \
                                self.p1Vida - self.p1VidaAntes == 0:
                                    self.p1Vida = self.p1Vida-self.p2Dano
        
            else:
                self.p1VidaAntes = self.p1Vida
        
        #Berserk - Aumenta o dano e velocidade de movimento por um breve momento(E)   
        if self.p2 == 1 and self.p2AtaqueN:
            if time() - self.duracaoCastN < 3:
                self.tela.blit(self.berserker, (self.xP2+10, self.yP2-50))
                self.p2Velocidade = 0.5
                self.p2Dano = 10
            else:
                self.p2Velocidade = self.p2VelocidadePadrao
                self.p2Dano = self.p2DanoPadrao
        
        #Jogador 1
        #Arqueiro
        #Ataque de flecha
        if self.p1 == 4 and self.p1AtaqueE:
            if time() - self.duracaoCastE < 0.2:
                pg.draw.circle(self.tela, (0,0,0), (self.xP1CirculoCentralizado, self.yP1CirculoCentralizado), self.raioATQProjetil, 5)
                #se o p2 está na área de alcance do ataque de projétil:
                if ((int(self.xP2) in range (int(self.xP1CirculoCentralizado - self.raioATQProjetil), int(self.xP1CirculoCentralizado 
                + self.raioATQProjetil)) or \
                    int(self.xP2+40) in range (int(self.xP1CirculoCentralizado-self.raioATQProjetil), int(self.xP1CirculoCentralizado
                    + self.raioATQProjetil))) and \
                        (int(self.yP2) in range (int(self.yP1CirculoCentralizado-self.raioATQProjetil), int(self.yP1CirculoCentralizado
                        +self.raioATQProjetil)) or \
                            int(self.yP2+55) in range (int(self.yP1CirculoCentralizado-self.raioATQProjetil), int(self.
                            yP1CirculoCentralizado+self.raioATQProjetil)))) and \
                                self.p2Vida - self.p2VidaAntes == 0:
                                    pg.draw.line(self.tela, (0,0,0), (self.xP2CirculoCentralizado, self.yP2CirculoCentralizado), (self.xP1CirculoCentralizado, self.yP1CirculoCentralizado), 3)
                                    self.p2Vida = self.p2Vida - self.p1Dano

            else:
                self.p2VidaAntes = self.p2Vida
        
        #Jogador 2
        #Arqueiro

        if self.p2 == 4 and self.p2AtaqueM:
            if time() - self.duracaoCastM < 0.2:
                pg.draw.circle(self.tela, (0,0,0), (self.xP2CirculoCentralizado, self.yP2CirculoCentralizado), self.raioATQProjetil, 5)
                #se o p1 está na área de alcance do ataque de projétil:
                if ((int(self.xP1) in range (int(self.xP2CirculoCentralizado - self.raioATQProjetil), int(self.xPQCirculoCentralizado 
                + self.raioATQProjetil)) or \
                    int(self.xP1+40) in range (int(self.xP2CirculoCentralizado-self.raioATQProjetil), int(self.xP2CirculoCentralizado
                    + self.raioATQProjetil))) and \
                        (int(self.yP1) in range (int(self.yP2CirculoCentralizado-self.raioATQProjetil), int(self.yP2CirculoCentralizado
                        +self.raioATQProjetil)) or \
                            int(self.yP1+55) in range (int(self.yP2CirculoCentralizado-self.raioATQProjetil), int(self.
                            yP2CirculoCentralizado+self.raioATQProjetil)))) and \
                                self.p1Vida - self.p1VidaAntes == 0:
                                    pg.draw.line(self.tela, (0,0,0), (self.xP1CirculoCentralizado, self.yP1CirculoCentralizado), (3,4), 3)
                                    self.p1Vida = self.p1Vida - self.p2Dano

            else:
                self.p1VidaAntes = self.p1Vida
        