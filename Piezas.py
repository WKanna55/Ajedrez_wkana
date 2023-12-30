import pygame
from PIL import Image

#piezas y movimientos
class King:
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
                # condicion si la ficha sale del tablero
                if self.rect.x < 0 or self.rect.y < 0 \
                        or self.rect.x > window_width or self.rect.y > window_height:
                    self.rect.x = self.pos_x_anterior
                    self.rect.y = self.pos_y_anterior

                self.rect.x = int(self.rect.x - (self.rect.x % (window_width // 8)))
                self.rect.y = int(self.rect.y - (self.rect.y % (window_height // 8)))
                self.dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x, mouse_y = event.pos
                self.rect.x = mouse_x + self.offset_x
                self.rect.y = mouse_y + self.offset_y

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Queen:
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
                # condicion si la ficha sale del tablero
                if self.rect.x < 0 or self.rect.y < 0 \
                        or self.rect.x > window_width or self.rect.y > window_height:
                    self.rect.x = self.pos_x_anterior
                    self.rect.y = self.pos_y_anterior

                self.rect.x = int(self.rect.x - (self.rect.x % (window_width // 8)))
                self.rect.y = int(self.rect.y - (self.rect.y % (window_height // 8)))
                self.dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x, mouse_y = event.pos
                self.rect.x = mouse_x + self.offset_x
                self.rect.y = mouse_y + self.offset_y

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Bishop:
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
                # condicion si la ficha sale del tablero
                if self.rect.x < 0 or self.rect.y < 0 \
                        or self.rect.x > window_width or self.rect.y > window_height:
                    self.rect.x = self.pos_x_anterior
                    self.rect.y = self.pos_y_anterior

                self.rect.x = int(self.rect.x - (self.rect.x % (window_width // 8)))
                self.rect.y = int(self.rect.y - (self.rect.y % (window_height // 8)))
                self.dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x, mouse_y = event.pos
                self.rect.x = mouse_x + self.offset_x
                self.rect.y = mouse_y + self.offset_y

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Knight:
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
                # condicion si la ficha sale del tablero
                if self.rect.x < 0 or self.rect.y < 0 \
                        or self.rect.x > window_width or self.rect.y > window_height:
                    self.rect.x = self.pos_x_anterior
                    self.rect.y = self.pos_y_anterior

                self.rect.x = int(self.rect.x - (self.rect.x % (window_width // 8)))
                self.rect.y = int(self.rect.y - (self.rect.y % (window_height // 8)))
                self.dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x, mouse_y = event.pos
                self.rect.x = mouse_x + self.offset_x
                self.rect.y = mouse_y + self.offset_y

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Rook:
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
                # condicion si la ficha sale del tablero
                if self.rect.x < 0 or self.rect.y < 0 \
                        or self.rect.x > window_width or self.rect.y > window_height:
                    self.rect.x = self.pos_x_anterior
                    self.rect.y = self.pos_y_anterior

                self.rect.x = int(self.rect.x - (self.rect.x % (window_width // 8)))
                self.rect.y = int(self.rect.y - (self.rect.y % (window_height // 8)))
                self.dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x, mouse_y = event.pos
                self.rect.x = mouse_x + self.offset_x
                self.rect.y = mouse_y + self.offset_y
                print("moving rook")

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Pawn:
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
                # condicion si la ficha sale del tablero
                if self.rect.x < 0 or self.rect.y < 0 \
                        or self.rect.x > window_width or self.rect.y > window_height:
                    self.rect.x = self.pos_x_anterior
                    self.rect.y = self.pos_y_anterior

                self.rect.x = int(self.rect.x - (self.rect.x % (window_width // 8)))
                self.rect.y = int(self.rect.y - (self.rect.y % (window_height // 8)))
                self.dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x, mouse_y = event.pos
                self.rect.x = mouse_x + self.offset_x
                self.rect.y = mouse_y + self.offset_y

    def draw(self, surface):
        surface.blit(self.image, self.rect)

def obtain_piece(image, position, piece_char):
    piece_char = piece_char.lower()
    pieza_retorno = {
        "k": King(image, position),
        "q": Queen(image, position),
        "b": Bishop(image, position),
        "n": Knight(image, position),
        "r": Rook(image, position),
        "p": Pawn(image, position)
    }

    return pieza_retorno[piece_char]


def pieza_de_piezas(image_path, chunk_width, chunk_height, new_size=None):
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
    piezas = pieza_de_piezas('images/piezas.png', chunk_width=334, chunk_height=334,
                             new_size=(window_width / 8, window_height / 8))
    blancas = []
    negras = []
    for i, pieza in enumerate(piezas):
        if i % 2 == 0:
            blancas.append(pieza)
        else:
            negras.append(pieza)
    return blancas, negras

def piezas_dict(window_width, window_height):
    p_blancas, p_negras = piezas_ajedrez(window_width, window_height)
    piezas = {
       "k": p_negras[0],
       "q": p_negras[1],
       "b": p_negras[2],
       "n": p_negras[3],
       "r": p_negras[4],
       "p": p_negras[5],
       "K": p_blancas[0],
       "Q": p_blancas[1],
       "B": p_blancas[2],
       "N": p_blancas[3],
       "R": p_blancas[4],
       "P": p_blancas[5]
       # Agrega más imágenes según sea necesario
    }

    return piezas
def mostrar_piezas(tablero_ordenado, piezas_img):
    piezas_pos = []
    for i in tablero_ordenado:
        for j in i:
            for k, v in j.items():
                if k != "":
                    piezas_pos.append(obtain_piece(piezas_img[k], v, k))
    return piezas_pos
