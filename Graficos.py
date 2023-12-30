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

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.dragging = True
                mouse_x, mouse_y = event.pos
                self.offset_x = self.rect.x - mouse_x
                self.offset_y = self.rect.y - mouse_y
                #print(self.offset_x) #posicion a la cual se inicia el agarre
                #print(self.offset_y) #posicion a la cual se inicia el agarre
                #print()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                #posicionar bien la ficha en le tablero
                #self.rect.x = self.rect.x
                #self.rect.y
                self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x, mouse_y = event.pos
                self.rect.x = mouse_x + self.offset_x
                self.rect.y = mouse_y + self.offset_y
                #print(self.rect.x) # movimiento de la ficha por el tablero
                #print(self.rect.y) # movimiento de la ficha por el tablero
                #print()

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

def piezas_ajedrez(screen, window_width, window_height):
    piezas = split_image_in_memory('images/piezas.png', chunk_width=334, chunk_height=334,
                                        new_size=(window_width / 8, window_height / 8))
    blancas = []
    negras = []
    for i, pieza in enumerate(piezas):
        if i % 2 == 0:
            blancas.append(pieza)
        else:
            negras.append(pieza)

    #for i, blanca in enumerate(blancas):
    #    screen.blit(blanca, (i * 100, 0))
    #for i, negra in enumerate(negras):
    #    screen.blit(negra, (i * 100, 700))

    return blancas, negras

