#Pregunta al usuario una asignatura e indica si está dentro del conjunto.
asignaturas = {"Matemáticas", "Física", "Química", "Programación"}

asignatura = input('Introduce una asignatura')

if asignatura in asignaturas:
    print('Existe')
else:
    print('No existe')
