def pide_palabra():
    palabra = input("Introduce una palabra: ")
    return palabra

def compara_raices(palabras):
    raiz = palabras[0]
    for palabra in palabras[1:]:
        while not palabra.startswith(raiz):
            raiz = raiz[:-1]
            print(f'Raíz común: {raiz}')
            if raiz == "":
                return ""
    return raiz

aux=0
palabra =[]
while True:
    palabra.append(pide_palabra())
    if palabra[aux] == "":  
        break
    else:
        aux += 1

palabra.pop()  # Eliminar la última palabra vacía

if (len(palabra) == 0):
    print("No se ingresaron palabras.")
else:
    raiz = compara_raices(palabra)

    if raiz == "":
        print("No hay raíz común.")
    else:
        print(f'La raíz común es: {raiz}')