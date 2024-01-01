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

print("origen:", origen)
print("destino:", destino)