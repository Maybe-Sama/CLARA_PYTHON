# 1. Obtén todos los alumnos que estudian al menos una de las dos asignaturas.
# 2. Obtén los alumnos que estudian Matemáticas pero no Física.
matematicas = {"Ana", "Luis", "Marta", "Carlos"}
fisica = {"Luis", "Carlos", "Pedro", "Lucía"}

todos = matematicas | fisica

solo_mates=matematicas - fisica

# A | B union
# A - B diferencia (Dejamos los que únicamente pertenecen a A)
# A & B intersección

print(todos)
print(solo_mates)


