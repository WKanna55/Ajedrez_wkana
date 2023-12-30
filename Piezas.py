import pygame

#piezas y movimientos
class Piezas:
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

    def obtain_piece(self, image, position, piece_char):
        piece_char = piece_char.lower()
        pieza_retorno = {
            "k": Piezas.King(image, position),
            "q": Piezas.Queen(image, position),
            "b": Piezas.Bishop(image, position),
            "n": Piezas.Knight(image, position),
            "r": Piezas.Rook(image, position),
            "p": Piezas.Pawn(image, position)
        }

        return pieza_retorno[piece_char]


