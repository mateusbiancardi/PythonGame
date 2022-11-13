import pygame as py

#PERSONAGEM DE ATAQUE FÍSICO
class Personagem:
    def __init__(self) :
        self.VIDA = 30
        self.VELOCIDADE = 0.5
    
    #área para acertar o boneco
    def hitbox(self):
        pass    
    
    def ataqueFisico(self):
        pass