import pygame as py

class Personagem:
    def __init__(self, escolhido) :
        self.personagem = escolhido
    
    #área para acertar o boneco
    def stats(self):
        if self.personagem == 1:
            
            VELOCIDADE = 0.5
            VIDA = 20
            self.status = (VELOCIDADE, VIDA)
            
        elif self.personagem == 2:
            
            VELOCIDADE = 0.3
            VIDA = 40
            self.status = (VELOCIDADE, VIDA)
            
        elif self.personagem == 3:
            
            VELOCIDADE = 0.5
            VIDA = 20
            self.status = (VELOCIDADE, VIDA)
            
        elif self.personagem == 4:
            
            VELOCIDADE = 0.3
            VIDA = 20
            self.status = (VELOCIDADE, VIDA)