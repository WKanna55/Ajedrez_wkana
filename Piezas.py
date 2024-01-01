import pygame
from PIL import Image

class Piezas_general:
    def __init__(self, image, position, tablero):
        self.image = image
        self.rect = image.get_rect(topleft=position)
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
        self.pos_x_anterior = 0
        self.pos_y_anterior = 0
        self.tablero = tablero

    def bring_to_front(self, images):
        """ Mueve esta pieza al frente de la lista. """
        images.remove(self)
        images.append(self)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

#piezas y movimientos
class King(Piezas_general):
    def handle_event(self, event, window_size):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                # movimiento libre de la pieza
                self.dragging = True
                mouse_x, mouse_y = event.pos
                self.offset_x = self.rect.x - mouse_x
                self.offset_y = self.rect.y - mouse_y
                self.pos_x_anterior = self.rect.x
                self.pos_y_anterior = self.rect.y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                # posicionamiento de la pieza
                self.rect.x += 50
                self.rect.y += 50
                # condicion si la ficha sale del tablero
                if self.rect.x < 0 or self.rect.y < 0 \
                        or self.rect.x > window_size or self.rect.y > window_size:
                    self.rect.x = self.pos_x_anterior
                    self.rect.y = self.pos_y_anterior

                self.rect.x = int(self.rect.x - (self.rect.x % (window_size // 8)))
                self.rect.y = int(self.rect.y - (self.rect.y % (window_size // 8)))
                self.dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x, mouse_y = event.pos
                self.rect.x = mouse_x + self.offset_x
                self.rect.y = mouse_y + self.offset_y

class Queen(Piezas_general):

    def handle_event(self, event, window_size):
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
                        or self.rect.x > window_size or self.rect.y > window_size:
                    self.rect.x = self.pos_x_anterior
                    self.rect.y = self.pos_y_anterior

                self.rect.x = int(self.rect.x - (self.rect.x % (window_size // 8)))
                self.rect.y = int(self.rect.y - (self.rect.y % (window_size // 8)))
                self.dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x, mouse_y = event.pos
                self.rect.x = mouse_x + self.offset_x
                self.rect.y = mouse_y + self.offset_y

class Bishop(Piezas_general):
    def handle_event(self, event, window_size):
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
                        or self.rect.x > window_size or self.rect.y > window_size:
                    self.rect.x = self.pos_x_anterior
                    self.rect.y = self.pos_y_anterior

                self.rect.x = int(self.rect.x - (self.rect.x % (window_size // 8)))
                self.rect.y = int(self.rect.y - (self.rect.y % (window_size // 8)))
                self.dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x, mouse_y = event.pos
                self.rect.x = mouse_x + self.offset_x
                self.rect.y = mouse_y + self.offset_y

class Knight(Piezas_general):
    def handle_event(self, event, window_size):
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
                        or self.rect.x > window_size or self.rect.y > window_size:
                    self.rect.x = self.pos_x_anterior
                    self.rect.y = self.pos_y_anterior

                self.rect.x = int(self.rect.x - (self.rect.x % (window_size // 8)))
                self.rect.y = int(self.rect.y - (self.rect.y % (window_size // 8)))
                self.dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x, mouse_y = event.pos
                self.rect.x = mouse_x + self.offset_x
                self.rect.y = mouse_y + self.offset_y

class Rook(Piezas_general):
    def handle_event(self, event, window_size):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                # click pieza
                self.dragging = True
                mouse_x, mouse_y = event.pos
                self.offset_x = self.rect.x - mouse_x
                self.offset_y = self.rect.y - mouse_y
                self.pos_x_anterior = self.rect.x
                self.pos_y_anterior = self.rect.y


        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                # posicion pieza
                self.rect.x += 50
                self.rect.y += 50
                # condicion si la ficha sale del tablero
                if self.rect.x < 0 or self.rect.y < 0 \
                        or self.rect.x > window_size or self.rect.y > window_size:
                    self.rect.x = self.pos_x_anterior
                    self.rect.y = self.pos_y_anterior

                self.rect.x = int(self.rect.x - (self.rect.x % (window_size // 8)))
                self.rect.y = int(self.rect.y - (self.rect.y % (window_size // 8)))

                self.tablero = Rook.mov_piece(self, (self.rect.x, self.rect.y), (self.pos_x_anterior, self.pos_y_anterior))
                self.dragging = False


        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                # arrastre
                mouse_x, mouse_y = event.pos
                self.rect.x = mouse_x + self.offset_x
                self.rect.y = mouse_y + self.offset_y
                #print("moving rook")

    def mov_piece(self, destino, origen):

        # Solo mover la pieza si está siendo arrastrada
        if self.dragging and Rook.is_mov_valid(self, destino, origen):
            indice_origen_y = origen[1] // 100
            indice_origen_x = origen[0] // 100
            indice_destino_y = destino[1] // 100
            indice_destino_x = destino[0] // 100

            print(indice_origen_y)
            print(indice_origen_x)
            print(indice_destino_y)
            print(indice_destino_x)


            # Acceder directamente a los elementos en self.tablero
            origen_tab = self.tablero[indice_origen_y][indice_origen_x]
            destino_tab = self.tablero[indice_destino_y][indice_destino_x]

            # Intercambiar las posiciones de las piezas en el tablero
            self.tablero[indice_origen_y][indice_origen_x], self.tablero[indice_destino_y][
                indice_destino_x] = destino_tab, origen_tab

            print("Tablero actualizado:")
            print(self.tablero)

        return self.tablero


    def is_mov_valid(self, destino, origen):

        return True


class Pawn(Piezas_general):
    def handle_event(self, event, window_size):
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
                        or self.rect.x > window_size or self.rect.y > window_size:
                    self.rect.x = self.pos_x_anterior
                    self.rect.y = self.pos_y_anterior

                self.rect.x = int(self.rect.x - (self.rect.x % (window_size // 8)))
                self.rect.y = int(self.rect.y - (self.rect.y % (window_size // 8)))
                self.dragging = False


        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x, mouse_y = event.pos
                self.rect.x = mouse_x + self.offset_x
                self.rect.y = mouse_y + self.offset_y


def obtain_piece(image, position, piece_char, tablero):
    piece_char = piece_char.lower()
    pieza_retorno = {
        "k": King(image, position, tablero),
        "q": Queen(image, position, tablero),
        "b": Bishop(image, position, tablero),
        "n": Knight(image, position, tablero),
        "r": Rook(image, position, tablero),
        "p": Pawn(image, position, tablero)
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


def piezas_ajedrez(window_size):
    piezas = pieza_de_piezas('images/piezas.png', chunk_width=334, chunk_height=334,
                             new_size=(window_size / 8, window_size / 8))
    blancas = []
    negras = []
    for i, pieza in enumerate(piezas):
        if i % 2 == 0:
            blancas.append(pieza)
        else:
            negras.append(pieza)
    return blancas, negras

def piezas_dict(window_size):
    p_blancas, p_negras = piezas_ajedrez(window_size)
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
                    piezas_pos.append(obtain_piece(piezas_img[k], v, k, tablero_ordenado))
    return piezas_pos

