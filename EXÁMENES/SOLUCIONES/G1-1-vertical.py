# Definir una versión **no recursiva** de la función.

datos = {"a": 3, "b": 19, "c": 8}

def histograma_vertical(d):

    claves = sorted(d.keys())
    altura = max(d.values())
  
    for i in range(altura, 0, -1):  
        for clave in claves:
            if d[clave] >= i:
                print(" * ", end="")
            else:
                print("   ", end="")
        print()

    print("".join(["---"] * len(claves)))
    
    for clave in claves:  
        print(f" {clave} ", end="")


histograma_vertical(datos)