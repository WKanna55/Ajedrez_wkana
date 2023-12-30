# Example file showing a circle moving on screen
import pygame
import Piezas
import Tablero
import os

# pygame setup
pygame.init()
window_width = 800
window_height = 800
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
running = True
dt = 0

"""generar cuadro para mover con drag and drop"""
# Crear las instancias de DraggableImage
"""graficos piezas"""
piezas_img = Piezas.piezas_dict(800,800)
tablero = Tablero.tablero_logico(800,800)
tablero = Tablero.posinicial_fen(tablero)

piezas_en_tablero = Piezas.mostrar_piezas(tablero, piezas_img)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Pasar el evento a cada imagen / movimiento
        for evento in piezas_en_tablero:
            evento.handle_event(event, window_width, window_height)

    """generar el tablero"""
    Tablero.dibujar_tablero(screen, window_width, window_height)

    """generar cuadro/imagen drag and drop || Dibujar el cuadro"""
    # Dibujar cada imagen
    for img in piezas_en_tablero:
        img.draw(screen)


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

