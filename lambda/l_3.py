
def sumar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def calcular(a, b, operacion):
    return operacion(a, b)


print(calcular(4, 3, sumar))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, lambda x, y: x - y))
