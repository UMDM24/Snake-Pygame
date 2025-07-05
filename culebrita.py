import pygame

class Personaje():
    def __init__(self, x, y):
        self.culebrita= pygame.Rect(0,0,20,20)
        self.culebrita.center=(x,y)
    
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, (255,255,255), self.culebrita)

    def movimiento(self,delta_x,delta_y):
        self.culebrita.x+=delta_x
        self.culebrita.y+=delta_y