notas = {
    "Ana": 8,
    "Luis": 5,
    "Marta": 9,
    "Carlos": 4
}

#for clave, valor in diccionario.items():

for nombre, nota in notas.items():
    print(nombre, "tiene un", nota)

#calculo de media

suma=0

for nota in notas.values(): #  notas.keys() para la clave
    suma+= nota

media = suma / len(notas)

print(f'La media es: {media}')