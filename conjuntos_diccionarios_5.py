#Calcula cuántas palabras diferentes aparecen
frase = "python es fácil y python es divertido"

palabras = frase.split()
print(palabras)
palabras_distintas = set(palabras)

print(palabras_distintas)
print("El número de palabras diferentes: ", len(palabras_distintas))