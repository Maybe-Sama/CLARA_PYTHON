def crear_tupla_tiempo():
    ruptor = 0
    tupla=['','','','']
    for i in range (3):
        if(i==0):
            print('Que tipo de cielo tenemos hoy?')
            print('1. Lluvia\n2. Soleado \n3. Nublado')
            aux1=int(input('Introduce 1, 2 o 3: '))
            while(ruptor == 0):
                if aux1 == 1:
                    
                    tupla[i]=('Lluvia')
                    print('lluvia')
                    ruptor = 1
                elif aux1==2 :
                    tupla[i]=('soleado')
                    print('soleado')
                    ruptor = 1
                elif aux1==3 :
                    tupla[i]=('nublado')
                    print('nublado')
                    ruptor = 1
                else:
                    aux1= int(input("Número introduci invalido. Introduce otro: "))
                    
        elif(i==1):
            print('Que tipo de humedad hace?')
            print('1. Alta\n2. Normal')
            aux1=int(input('Introduce 1, 2: '))
            while(ruptor == 0):
                if aux1 == 1:
                    tupla[i]=('Alta')
                    print('Alta')
                    ruptor = 1
                elif aux1==2 :
                    tupla[i]=('Normal')
                    print('Normal')
                    ruptor = 1
                else:
                    aux1= int(input("Número introduci invalido. Introduce otro: "))  


        elif(i==2):
            print('Qué tipo de viento hace hoy?')
            print('1. Fuerte\n2. Débil')
            aux1=int(input('Introduce 1, 2: '))
            while(ruptor == 0):
                if aux1 == 1:
                    tupla[i]=('Fuerte')
                    print('Fuerte')
                    ruptor = 1
                elif aux1==2 :
                    tupla[i]=('Débil')
                    print('Débil')
                    ruptor = 1
                else:
                    aux1= int(input("Número introduci invalido. Introduce otro: ")) 

    return tupla
    

print(crear_tupla_tiempo())


