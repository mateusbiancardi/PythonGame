import pygame as py

class Personagem:
    def __init__(self, escolhido) :
        self.personagem = escolhido
    
    #área para acertar o boneco
    def stats(self):
        
        #guerreiro
        if self.personagem == 1:
            
            VELOCIDADE = 0.4
            VIDA = 40
            VELOCIDADE_ATQ = 2
            DANO = 5
            self.status = (VELOCIDADE, VIDA, 1)
          
        #mago  
        elif self.personagem == 2:
            
            VELOCIDADE = 0.5
            VIDA = 20
            VELOCIDADE_ATQ = 2
            DANO = 4
            self.status = (VELOCIDADE, VIDA, 2)
          
        #xamã  
        elif self.personagem == 3:
            
            VELOCIDADE = 0.5
            VIDA = 30
            VELOCIDADE_ATQ = 4
            DANO = 5
            self.status = (VELOCIDADE, VIDA, 3)
          
        #arqueiro  
        elif self.personagem == 4:
            
            VELOCIDADE = 0.5
            VIDA = 25
            VELOCIDADE_ATQ = 1
            DANO = 3
            self.status = (VELOCIDADE, VIDA, 4)