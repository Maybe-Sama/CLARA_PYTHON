numeros = int(input("Introduce la cantidad de números: "))
lista = ['']*numeros #lista = ['','','','','','']

#lista = ['']*int(input("Introduce la cantidad de números: "))  #forma PRO

for n in range(numeros):
    lista[n]=int(input(f'Introduce el valor {n+1}: '))

print(lista)
