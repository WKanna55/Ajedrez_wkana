# Example file showing a circle moving on screen
import pygame
from PIL import Image
import Graficos
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
p_blancas, p_negras = Graficos.piezas_ajedrez(screen, window_width, window_height)
images = [
    Graficos.DraggableImage(p_blancas[0], (100, 100)),
    Graficos.DraggableImage(p_blancas[1], (300, 200)),
    # Agrega más imágenes según sea necesario
]


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Pasar el evento a cada imagen / movimiento
        for img in images:
            img.handle_event(event)

    """generar el tablero"""
    Graficos.dibujar_tablero(screen, window_width, window_height)

    """generar cuadro/imagen drag and drop || Dibujar el cuadro"""
    # Dibujar cada imagen
    for img in images:
        img.draw(screen)


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

