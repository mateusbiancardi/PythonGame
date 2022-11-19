import pygame as pg
import sys
from configJogo import ConfigJogo
from selecaoPersonagem import telaSelecao
from personagens import Personagem

class telaPrincipal():
    def __init__(self, tela, escolhidos):
        self.tela = tela
        self.encerrada = False
        
        p1 = Personagem(escolhidos[0])
        p2 = Personagem(escolhidos[1])
        
        p1.stats()
        p2.stats()
        
        self.p1Velocidade = p1.status[0]
        self.p2Velocidade = p2.status[0]
        
        #depois que implementar os personagens, fazer todas as mudanças
        ##self.velocidadePerso = 0.3
        
        self.xP1 = ConfigJogo.LARGURA_TELA * (1/3)
        self.yP1 = ConfigJogo.ALTURA_TELA // 2
        self.v_xP1 = 0
        self.v_yP1 = 0
        
        self.xP2 = ConfigJogo.LARGURA_TELA * (2/3)
        self.yP2 = ConfigJogo.ALTURA_TELA // 2
        self.v_xP2 = 0
        self.v_yP2 = 0
    
    def rodar(self):
        while not self.encerrada:
            self.tela.fill((102, 255, 51))
            self.tratamentoEventos()
            self.movimento()
            self.personagem1()
            self.personagem2()
            
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
        self.xP1 += self.v_xP1
        self.yP1 += self.v_yP1
        
        self.xP2 += self.v_xP2
        self.yP2 += self.v_yP2
    
    def personagem1 (self):
        pg.draw.rect(
                self.tela, 
                (0,0,0),
                pg.Rect(self.xP1, self.yP1, 50, 50)
        )
    def personagem2 (self):
        pg.draw.rect(
                self.tela, 
                (0,0,0),
                pg.Rect(self.xP2, self.yP2, 50, 50)
        )