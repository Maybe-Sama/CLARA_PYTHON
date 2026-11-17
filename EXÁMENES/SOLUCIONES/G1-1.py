# Definir una versión **no recursiva** de la función.

datos = {"a": 3, "b": 19, "c": 8}

def histograma_horizontal(d):
    for clave, valor in sorted(d.items()):
        print(f"{clave}:{'*'*valor}")
        
histograma_horizontal(datos)