import pygame

class Manzana():
    def __init__(self, x, y):
        self.manzana= pygame.Rect(0,0,20,20)
        self.manzana.center=(x,y)
    
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, (255,0,0), self.manzana)