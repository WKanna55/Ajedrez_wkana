import pygame
from PIL import Image

# clase para arrastrar imagenes
class DraggableImage:
    def __init__(self, image, position):
        self.image = image
        self.rect = image.get_rect(topleft=position)
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
        self.pos_x_anterior = 0
        self.pos_y_anterior = 0

    def handle_event(self, event, window_width, window_height):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.dragging = True
                mouse_x, mouse_y = event.pos
                self.offset_x = self.rect.x - mouse_x
                self.offset_y = self.rect.y - mouse_y
                self.pos_x_anterior = self.rect.x
                self.pos_y_anterior = self.rect.y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.rect.x += 50
                self.rect.y += 50
                #condicion si la ficha sale del tablero
                if self.rect.x < 0 or self.rect.y < 0 \
                        or self.rect.x > window_width or self.rect.y > window_height:
                    self.rect.x = self.pos_x_anterior
                    self.rect.y = self.pos_y_anterior

                self.rect.x = int(self.rect.x - (self.rect.x % (window_width//8)))
                self.rect.y = int(self.rect.y - (self.rect.y % (window_height//8)))
                self.dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x, mouse_y = event.pos
                self.rect.x = mouse_x + self.offset_x
                self.rect.y = mouse_y + self.offset_y


    def draw(self, surface):
        surface.blit(self.image, self.rect)


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

def piezas_ajedrez(window_width, window_height):
    piezas = split_image_in_memory('images/piezas.png', chunk_width=334, chunk_height=334,
                                        new_size=(window_width / 8, window_height / 8))
    blancas = []
    negras = []
    for i, pieza in enumerate(piezas):
        if i % 2 == 0:
            blancas.append(pieza)
        else:
            negras.append(pieza)
    return blancas, negras

