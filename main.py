#librerias
import pygame
import sys
from culebrita import Personaje
from manzanas import Manzana
import random

pygame.init()
#Personaje ubicacion inicial
personaje= Personaje(50,50)

#dimensiones de la ventana
ancho,alto = 800,600

manzanas=[]
hay_manzana=True
ventana = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("Juego de la culebrita")

manzanas.append(Manzana(ancho / 2, 100))


def crear_manzanas():
    global hay_manzana
    
    if hay_manzana:
        manzanas.append(Manzana(random.randint(75,ancho-75),random.randint(75,alto-75)))
        

manzanas.append(Manzana(ancho / 2, 100))
#variables de movimiento
izquierda=False
derecha=False
arriba=False
abajo=False
#variables de direccion
delta_x = 0
delta_y = 0

jugando=True
reloj=pygame.time.Clock()
while jugando:

    
    #manejo de FPS
    reloj.tick(30)
    #background
    ventana.fill((0,0,20) )

    #condicionales de movimiento
    if derecha :
        delta_x=5
        delta_y=0
    elif izquierda :
        delta_x=-5
        delta_y=0
    elif arriba:
        delta_y=-5
        delta_x=0
    elif abajo:
        delta_y=5
        delta_x=0

    personaje.movimiento(delta_x,delta_y)

    personaje.dibujar(ventana)
    
    for event in pygame.event.get():
        if event.type== pygame.QUIT  :
            jugando=False
            sys.exit()
        if event.type== pygame.KEYDOWN:
            if event.key==pygame.K_a and derecha!=True:
                izquierda=True
                abajo=False
                arriba=False
            if event.key==pygame.K_d and izquierda!=True:
                derecha=True
                abajo=False
                arriba=False
            if event.key==pygame.K_w and abajo!=True:
                arriba=True
                izquierda=False
                derecha=False
            if event.key==pygame.K_s and arriba!=True:
                abajo=True
                izquierda=False
                derecha=False
        
    for manzana in manzanas[:]:
        manzana.dibujar(ventana)
         
        # Colisión manzana
        if pygame.Rect.colliderect(manzana.manzana, personaje.culebrita):
            manzanas.remove(manzana)
            hay_manzana=False
            

    if not hay_manzana:
        hay_manzana=True
        crear_manzanas()
        
    
    pygame.display.update()

pygame.quit()