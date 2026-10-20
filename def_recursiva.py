# Crea una función recursiva que calcule la suma de los números desde 1 hasta n
#NORMAL
#def suma(n):
#    if n == 1:
#        return 1
#    aux= n + suma(n-1) 
#    print(n)
#    return aux 

#print(suma(5))

#suma(5)
#=5+suma(4)
#=5+4+suma(3)
#=5+4+3+suma(2)
#=suma 5+4+3+2+suma(1) = 15


#COLA
#def suma(n, aux2=0):
#    if n == 0:
#        return aux2
#    
#    return suma(n-1, aux2 +n)

#print(suma(5))

#suma(5,0)
#suma(4,5)
#suma(3,9)
#suma(2,12)
#suma(1,14)
#suma(0,15)
#--->15

#MÚLTIPLE
def fibonacci(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
   
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(8))
