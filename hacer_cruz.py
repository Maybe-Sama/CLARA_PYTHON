def aspa(altura, caracter):
    for i in range(altura):
        for j in range(altura):
            if i==j or i+j == altura -1:
                print(caracter, end='')
            else:
                print('  ', end='')
        print()

aspa(7,'*')

