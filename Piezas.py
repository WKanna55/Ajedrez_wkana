import pygame
from PIL import Image

class Piezas_general:
    def __init__(self, image, position, tablero, wrapper):
        self.image = image
        self.rect = image.get_rect(topleft=position)
        print(self.rect)
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
        self.pos_x_anterior = 0
        self.pos_y_anterior = 0
        self.tablero = tablero
        self.wrapper = wrapper

    def bring_to_front(self, images):
        """ Mueve esta pieza al frente de la lista. """
        images.remove(self)
        images.append(self)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def tramo(self):
        pass

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
                Rook.mov_piece(self, window_size)


        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                # arrastre
                mouse_x, mouse_y = event.pos
                self.rect.x = mouse_x + self.offset_x
                self.rect.y = mouse_y + self.offset_y
                #print("moving rook")


    def mov_piece(self, window_size):
        self.rect.x += 50
        self.rect.y += 50

        # condicion si la ficha sale del tablero
        if self.rect.x < 0 or self.rect.y < 0 \
                or self.rect.x > window_size or self.rect.y > window_size and self.dragging:
            self.rect.x = self.pos_x_anterior
            self.rect.y = self.pos_y_anterior
            self.dragging = False

        self.rect.x = int(self.rect.x - (self.rect.x % (window_size // 8)))
        self.rect.y = int(self.rect.y - (self.rect.y % (window_size // 8)))

        if (self.is_mov_valid((self.rect.x, self.rect.y), (self.pos_x_anterior, self.pos_y_anterior))
                and self.dragging):

            self.tablero = self.actualizar_tablero((self.rect.x, self.rect.y),
                                               (self.pos_x_anterior, self.pos_y_anterior))

            self.dragging = False
        elif self.dragging:
            self.rect.x = self.pos_x_anterior
            self.rect.y = self.pos_y_anterior
            self.dragging = False


    def actualizar_tablero(self, destino, origen):

        # Solo mover la pieza si está siendo arrastrada
        if self.dragging and Rook.is_mov_valid(self, destino, origen):
            indice_origen_y = origen[1] // 100
            indice_origen_x = origen[0] // 100
            indice_destino_y = destino[1] // 100
            indice_destino_x = destino[0] // 100

            # Acceder directamente a los elementos en self.tablero
            origen_tab = self.tablero[indice_origen_y][indice_origen_x]
            destino_tab = self.tablero[indice_destino_y][indice_destino_x]
            print(origen_tab)
            print(destino_tab)

            origen_tab_key, origen_tab_value = next(iter(origen_tab.items()))
            destino_tab_key, destino_tab_value = next(iter(destino_tab.items()))

            self.tablero[indice_origen_y][indice_origen_x][destino_tab_key] = self.tablero[indice_origen_y][indice_origen_x].pop(origen_tab_key)
            self.tablero[indice_destino_y][indice_destino_x][origen_tab_key] = self.tablero[indice_destino_y][indice_destino_x].pop(destino_tab_key)
            print("Tablero actualizado:")
            print(self.tablero)

        elif self.dragging:

            print("No se actualizo")

        return self.tablero


    def is_mov_valid(self, destino, origen):

        # Solo mover la pieza si está siendo arrastrada
        if self.dragging:
            indice_origen_y = origen[1] // 100
            indice_origen_x = origen[0] // 100
            indice_destino_y = destino[1] // 100
            indice_destino_x = destino[0] // 100

            #condicion para mover
            if indice_origen_y == indice_destino_y or indice_origen_x == indice_destino_x:
                return self.piece_trail_valid(destino, origen)
            else:
                return False

    def piece_trail_valid(self, destino, origen):
        if self.dragging:
            indice_origen_y = origen[1] // 100
            indice_origen_x = origen[0] // 100
            indice_destino_y = destino[1] // 100
            indice_destino_x = destino[0] // 100

            print(f"origeny: {indice_origen_y} || origenx: {indice_origen_x}\ndestinoy: {indice_destino_y} || destinox: {indice_destino_x}")
            #print()

            pieza_origen, pos_origen = next(iter(self.tablero[indice_origen_y][indice_origen_x].items()))
            pieza_destino, pos_destino = next(iter(self.tablero[indice_destino_y][indice_destino_x].items()))

            print(f"pieza: {pieza_origen} || posicion: {pos_origen} || Negra?: {pieza_origen.islower()}")


            rango_y = abs(indice_destino_y - indice_origen_y) + 1
            rango_x = abs(indice_destino_x - indice_origen_x) + 1
            print(f"rangoy: {rango_y} || rangox: {rango_x}")

            mov_vertical = indice_origen_x == indice_destino_x
            mov_horizontal = indice_origen_y == indice_destino_y

            print(f"es vertical: {mov_vertical} || es horizontal: {mov_horizontal}")

            bandera_aliado = 0
            bandera_enemigo = 0
            if mov_vertical:
                if indice_origen_y < indice_destino_y:
                    for y in range(1, rango_y):
                        ver_pieza = self.tablero[indice_origen_y+y][indice_destino_x]
                        pieza, pos = next(iter(ver_pieza.items()))
                        if self.piece_ally(pieza, pieza_origen):
                            #print(self.piece_ally(pieza, pieza_origen))
                            bandera_aliado += 1
                        if self.piece_enemy(pieza, pieza_origen):
                            bandera_enemigo += 1
                        print(f"pieza: {pieza}, posicion: {pos}")
                    print("iteracion completada\n")
                else:
                    for y in range(1, rango_y):
                        iterador_y = max(indice_origen_y, indice_destino_y) - y
                        print(iterador_y)
                        ver_pieza = self.tablero[iterador_y][indice_destino_x]
                        pieza, pos = next(iter(ver_pieza.items()))
                        if self.piece_ally(pieza, pieza_origen):
                            #print(self.piece_ally(pieza, pieza_origen))
                            bandera_aliado += 1
                        if self.piece_enemy(pieza, pieza_origen):
                            bandera_enemigo += 1
                        print(f"pieza: {pieza}, posicion: {pos}")
                    print("iteracion completada\n")

            elif mov_horizontal:
                if indice_origen_x < indice_destino_x:
                    for x in range(1, rango_x):
                        ver_pieza = self.tablero[indice_destino_y][x]
                        pieza, pos = next(iter(ver_pieza.items()))
                        if self.piece_ally(pieza, pieza_origen):
                            #print(self.piece_ally(pieza, pieza_origen))
                            bandera_aliado += 1
                        if self.piece_enemy(pieza, pieza_origen):
                            bandera_enemigo += 1
                        print(f"pieza: {pieza}, posicion: {pos}")
                    print("iteracion completada\n")
                else:
                    for x in range(1, rango_x):
                        iterador_x = max(indice_origen_x, indice_destino_x) - x
                        ver_pieza = self.tablero[indice_destino_y][iterador_x]
                        pieza, pos = next(iter(ver_pieza.items()))
                        if self.piece_ally(pieza, pieza_origen):
                            #print(self.piece_ally(pieza, pieza_origen))
                            bandera_aliado += 1
                        if self.piece_enemy(pieza, pieza_origen):
                            bandera_enemigo += 1
                        print(f"pieza: {pieza}, posicion: {pos}")
                    print("iteracion completada\n")

            if bandera_enemigo == 1:
                self.wrapper.piezas_list = self.wrapper.eliminar_pieza(pos_destino)


            return bandera_aliado == 0 and bandera_enemigo <= 1


    def piece_ally(self, pieza_revisando, pieza_char):
        is_black = pieza_char.islower()
        if is_black:
            if pieza_revisando.islower():
                return True
        else:
            if pieza_revisando.isupper():
                return True
        return False


    def piece_enemy(self, pieza_revisando, pieza_char):
        is_black = pieza_char.islower()
        if is_black:
            if pieza_revisando.isupper():
                return True
        else:
            if pieza_revisando.islower():
                return True
        return False

    def kill_enemy_piece(self, target_pos):
        pass

    def cut_pass_piece(self, destino, origen):
        pass

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




class Piezas_wrapper:
    def __init__(self, image_path, window_size, tablero):
        self.image_path = image_path
        self.window_size = window_size
        self.tablero = tablero
        self.piezas_list = self.inicializar_piezas()

    def split_chunks_piezas(self, chunk_width, chunk_height, new_size=None):
        image = Image.open(self.image_path)
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

    def piezas_ajedrez_img(self):
        #piezas = split_chunks_piezas('images/piezas.png', chunk_width=334, chunk_height=334,
        #                             new_size=(self.window_size / 8, self.window_size / 8))
        piezas = self.split_chunks_piezas( chunk_width=334, chunk_height=334,
                                     new_size=(self.window_size / 8, self.window_size / 8))
        blancas = []
        negras = []
        for i, pieza in enumerate(piezas):
            if i % 2 == 0:
                blancas.append(pieza)
            else:
                negras.append(pieza)
        return blancas, negras

    def piezas_dict(self):
        p_blancas, p_negras = self.piezas_ajedrez_img()
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

    def obtain_piece(self, image, position, piece_char):
        piece_char = piece_char.lower()
        pieza_retorno = {
            "k": King(image, position, self.tablero.tablero_logico, self),
            "q": Queen(image, position, self.tablero.tablero_logico, self),
            "b": Bishop(image, position, self.tablero.tablero_logico, self),
            "n": Knight(image, position, self.tablero.tablero_logico, self),
            "r": Rook(image, position, self.tablero.tablero_logico, self),
            "p": Pawn(image, position, self.tablero.tablero_logico, self)
        }

        return pieza_retorno[piece_char]

    def inicializar_piezas(self):
        piezas_img = self.piezas_dict()
        piezas_class_list = []
        for i in self.tablero.tablero_logico:
            for j in i:
                for k, v in j.items():
                    if k != "":
                        piezas_class_list.append(self.obtain_piece(piezas_img[k], v, k))
        return piezas_class_list


    def eliminar_pieza(self, position):
        for i in self.piezas_list:
            if i.rect.y == position[1] and i.rect.x == position[0]:
                self.piezas_list.remove(i)
                break
        return self.piezas_list

