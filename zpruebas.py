x = 800 - (800 % 100)
#print(x)
inicial_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
lol = inicial_fen.split("/")
#print(lol)

#hola = "R"
#hola = hola.lower()
#print(hola)

origen = {"h": 2}
destino = {"": 5}

# Guardar temporalmente la clave y el valor de 'origen'
(origen_key, origen_value), = origen.items()

# Guardar temporalmente la clave y el valor de 'destino'
(destino_key, destino_value), = destino.items()

# Intercambiar las claves y valores
origen = {destino_key: origen_value}
destino = {origen_key: destino_value}

#print("origen:", origen)
#print("destino:", destino)

#for i in range(2,5+1):
#    for j in range(3,3+1):
#        print(f"i: {i} | j: {j}")
#
#cadena = "R"
#
#print(cadena.isupper())
#destino = 0
#origen = 7
#trazo = -7
#
#for i in range(7):
#    print(abs(trazo)-i-1)

#tuplaa = (0, 100)
#print(tuplaa[1])

class Auto:
    def __init__(self, marca):
        self.marca = marca

listaxd = [Auto("toyota"), Auto("mitsubishi")]
print(listaxd)
cadd = "toyota"
for i in listaxd:
    if i.marca == cadd:
        listaxd.remove(i)


print(listaxd)