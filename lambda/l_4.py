jugadores = [
    ("Carlos", 12, 5),
    ("Pedro", 8, 11),
    ("Luis", 20, 3),
    ("Mario", 15, 8)
]

ordenados = sorted (jugadores, key=lambda jugador: jugador[1], reverse=True)

print(ordenados)

mejor_asis= max(jugadores, key=lambda jugador: jugador[2])

print(mejor_asis[0])

