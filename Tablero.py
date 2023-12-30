import pygame
import random
import Piezas

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


def tablero_logico(window_width, window_height):
    tablero = []
    for i in range(8):
        tablero.append([])
        for j in range(8):
            tablero[i].append({"": (j*(window_height//8), i*(window_width//8))})

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


#piezas_img = piezas_dict(800,800)
#tablero = tablero_logico(800,800)
#tablero = posinicial_fen(tablero)
#
#piezas_en_tablero = mostrar_piezas(tablero, piezas_img)
#print(piezas_en_tablero)
