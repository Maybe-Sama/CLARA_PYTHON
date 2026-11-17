
def determinante_m(m):
    n = len(m)

    if n == 1:
        return m[0][0]

    if n == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    det = 0

    for j in range(n):
        # Matriz menor: eliminamos la primera fila y la columna j
        menor = [fila[:j] + fila[j + 1:] for fila in m[1:]]

        det += ((-1) ** j) * m[0][j] * determinante_m(menor)

    return det


print(determinante_m([[1, 2, -1,4], [4, 5, 6, 7], [7, 5, 9, 10], [1, 2, 3, 4]]))
