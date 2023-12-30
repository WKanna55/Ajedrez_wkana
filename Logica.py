import pygame
import random
import Graficos
import Piezas

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

def piezas_dict(window_width, window_height):
    p_blancas, p_negras = Graficos.piezas_ajedrez(window_width, window_height)
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

def mostrar_piezas(tablero_ordenado, piezas_img):
    piezas_pos = []
    for i in tablero_ordenado:
        for j in i:
            for k, v in j.items():
                if k != "":
                    piezas_pos.append(Piezas.Piezas().obtain_piece(piezas_img[k], v, k))
    return piezas_pos


#piezas_img = piezas_dict(800,800)
#tablero = tablero_logico(800,800)
#tablero = posinicial_fen(tablero)
#
#piezas_en_tablero = mostrar_piezas(tablero, piezas_img)
#print(piezas_en_tablero)
