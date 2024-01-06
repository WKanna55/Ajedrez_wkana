import pygame
import random
import Piezas

class Tablero:
    def __init__(self, screen, window_size, color1, color2):
        self.screen = screen
        self.window_size = window_size
        self.color1 = color1
        self.color2 = color2
        self.tablero_logico = Tablero.tablero_logico(self.window_size)
        self.tablero_logico = Tablero.posinicial_fen(self.tablero_logico)

    #def mov_piece(self):
    #    #is valid = True
    #    x = 150
    #    y = 47
    #    vect_click = [x,y]
    #    x1 = 46
    #    y1 = 265
    #    vect_drag_pull = [x1, y1]

    def dibujar_tablero(self):
        fila = 0
        columna = 0
        blanco = True
        for i in range(8):
            for j in range(8):
                if blanco:
                    pygame.draw.rect(self.screen, self.color1, (columna, fila, self.window_size / 8, self.window_size / 8))
                    blanco = False
                else:
                    pygame.draw.rect(self.screen, self.color2, (columna, fila, self.window_size / 8, self.window_size / 8))
                    blanco = True
                columna += self.window_size / 8
            if blanco:
                blanco = False
            else:
                blanco = True
            columna = 0
            fila += self.window_size / 8

    def dibujar_tramo_pieza(self, pieza_dic, pieza_list):
        pieza, pos = next(iter(pieza_dic))
        for i in range(len(pieza_list)):
            if pieza_list[i].rect.x == pos[1] and pieza_list[i].rect.y == pos[0]:
                #pieza_list[i].tramo #es una lista con tuplas de posiciones posibles para movimiento
                pass

    @staticmethod
    def tablero_logico(window_size):
        tablero = []
        for i in range(8):
            tablero.append([])
            for j in range(8):          # j = x : horizontal , i = y : vertical
                tablero[i].append({"": (j * (window_size // 8), i * (window_size // 8))})
        return tablero

    @staticmethod
    def copiar_tablero(tablero):
        tab2 = []
        for i in tablero:
            tab2.append(i)
        return tab2

    @staticmethod
    def posinicial_fen(tablero_log):
        inicial_fen = "rnbqkbnr/1pppppp1/8/8/8/8/1PPPPPP1/RNBQKBNR"
        split_inicial = inicial_fen.split("/")
        for i, fen in enumerate(split_inicial):
            j = 0
            for piece in fen:
                if piece.isdigit():
                    j += int(piece) - 1
                else:
                    tablero_log[i][j][piece] = tablero_log[i][j].pop("")
                j += 1
        return tablero_log


#nuevo_tab = Tablero(800, "black", "white")
#print(nuevo_tab.tablero_logico)
