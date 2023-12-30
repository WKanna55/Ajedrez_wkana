import pygame
import random
import Piezas

class Tablero:
    def __init__(self, window_size, color1, color2):
        self.window_size = window_size
        self. color1 = color1
        self.color2 = color2
        self.tablero_logico = tablero_logico(self.window_size)
        self.tablero_logico = posinicial_fen(self.tablero_logico)

    def mov_piece(self):
        #is valid = True
        x = 150
        y = 47
        vect_click = [x,y]
        x1 = 46
        y1 = 265
        vect_drag_pull = [x1, y1]
        






#tablero ajedrez
def dibujar_tablero(screen, window_size):
    fila = 0
    columna = 0
    blanco = True
    for i in range(8):
        for j in range(8):
            if blanco:
                pygame.draw.rect(screen, "purple", (columna, fila, window_size / 8, window_size / 8))
                blanco = False
            else:
                pygame.draw.rect(screen, "pink", (columna, fila, window_size / 8, window_size / 8))
                blanco = True
            columna += window_size / 8
        if blanco:
            blanco = False
        else:
            blanco = True
        columna = 0
        fila += window_size / 8


def tablero_logico(window_size):
    tablero = []
    for i in range(8):
        tablero.append([])
        for j in range(8):
            tablero[i].append({"": (j*(window_size//8), i*(window_size//8))})

    return tablero

def copiar_tablero(tablero):
    tab2 = []
    for i in tablero:
        tab2.append(i)
    return tab2

def posinicial_fen(tablero_log):
    inicial_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
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

nuevo_tab = Tablero(800, "black", "white")
print(nuevo_tab.tablero_logico)
