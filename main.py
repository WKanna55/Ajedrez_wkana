# Example file showing a circle moving on screen
import pygame
import Piezas
from Tablero import *
import os

# pygame setup
pygame.init()
window_size = 800
screen = pygame.display.set_mode((window_size, window_size))
clock = pygame.time.Clock()
running = True
dt = 0

"""generar cuadro para mover con drag and drop"""
"""graficos piezas"""
piezas_img = Piezas.piezas_dict(window_size)
#tablero = Tablero.tablero_logico(window_size)
#tablero = Tablero.posinicial_fen(tablero)

tableromain = Tablero(screen, window_size, "black", "white")

piezas_en_tablero = Piezas.mostrar_piezas(tableromain.tablero_logico, piezas_img)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Pasar el evento a cada imagen / movimiento
        for evento in piezas_en_tablero:
            evento.handle_event(event, window_size)
            if evento.dragging:
                evento.bring_to_front(piezas_en_tablero)

    """generar el tablero"""
    #Tablero.dibujar_tablero(screen, window_size)
    tableromain.dibujar_tablero()

    """generar cuadro/imagen drag and drop || Dibujar el cuadro"""
    for img in piezas_en_tablero:
        img.draw(screen)





    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

