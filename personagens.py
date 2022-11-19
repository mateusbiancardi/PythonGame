import pygame as py

#PERSONAGEM DE ATAQUE FÍSICO
class Personagem:
    def __init__(self, escolhido) :
        self.personagem = escolhido
    
    #área para acertar o boneco
    def stats(self):
        if self.personagem == 1:
            
            VELOCIDADE = 0.7
            VIDA = 20
            self.status = (VELOCIDADE, VIDA)
            
        elif self.personagem == 2:
            
            VELOCIDADE = 0.3
            VIDA = 20
            self.status = (VELOCIDADE, VIDA)