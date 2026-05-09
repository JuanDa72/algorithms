def matrix_multiply_dc(A, B):
    n = len(A)

    # Caso base: matriz 1x1
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Dividir matrices en 4 submatrices cada una
    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Llamadas recursivas para las multiplicaciones
    # C11 = A11*B11 + A12*B21
    C11 = add_matrices(
        matrix_multiply_dc(A11, B11),
        matrix_multiply_dc(A12, B21)
    )

    # C12 = A11*B12 + A12*B22
    C12 = add_matrices(
        matrix_multiply_dc(A11, B12),
        matrix_multiply_dc(A12, B22)
    )

    # C21 = A21*B11 + A22*B21
    C21 = add_matrices(
        matrix_multiply_dc(A21, B11),
        matrix_multiply_dc(A22, B21)
    )

    # C22 = A21*B12 + A22*B22
    C22 = add_matrices(
        matrix_multiply_dc(A21, B12),
        matrix_multiply_dc(A22, B22)
    )

    # Combinar las submatrices en la matriz resultante
    return combine_submatrices(C11, C12, C21, C22)


def add_matrices(A, B):
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]

    return result


def combine_submatrices(C11, C12, C21, C22):
    n = len(C11)
    size = 2 * n
    C = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(n):
        for j in range(n):
            C[i][j] = C11[i][j]

    for i in range(n):
        for j in range(n):
            C[i][j + n] = C12[i][j]

    for i in range(n):
        for j in range(n):
            C[i + n][j] = C21[i][j]

    for i in range(n):
        for j in range(n):
            C[i + n][j + n] = C22[i][j]

    return C


# Función auxiliar para probar
def print_matrix(matrix):
    for row in matrix:
        print([f"{x:3}" for x in row])


A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

B = [
    [16, 15, 14, 13],
    [12, 11, 10, 9],
    [8, 7, 6, 5],
    [4, 3, 2, 1]
]

print(matrix_multiply_dc(A,B))
