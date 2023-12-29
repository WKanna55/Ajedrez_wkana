import pygame
from PIL import Image

# tablero ajedrez
def dibujar_tablero(screen, window_width, window_height):
    fila = 0
    columna = 0
    blanco = True
    for i in range(8):
        for j in range(8):
            if blanco:
                pygame.draw.rect(screen, "purple", (columna, fila, window_width / 8, window_height / 8))
                blanco = False
            else:
                pygame.draw.rect(screen, "pink", (columna, fila, window_width / 8, window_height / 8))
                blanco = True
            columna += window_height / 8
        if blanco:
            blanco = False
        else:
            blanco = True
        columna = 0
        fila += window_width / 8


#graficos piezas
def split_image_in_memory(image_path, chunk_width, chunk_height, new_size=None):
    image = Image.open(image_path)
    chunks = []

    width, height = image.size
    for i in range(0, width, chunk_width):
        for j in range(0, height, chunk_height):
            box = (i, j, min(i + chunk_width, width), min(j + chunk_height, height))
            chunk = image.crop(box)
            mode = chunk.mode
            size = chunk.size
            data = chunk.tobytes()

            chunk = pygame.image.fromstring(data, size, mode)
            if new_size:
                chunk = pygame.transform.scale(chunk, new_size)
            chunks.append(chunk)

    return chunks


