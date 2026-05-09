import math
def strassen_matrix_multiply(A, B):
    """
    Multiplicación de matrices usando el algoritmo de Strassen
    Asume matrices cuadradas n x n donde n es potencia de 2
    """
    n = len(A)

    # Caso base: matriz 1x1
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Dividir matrices en 4 submatrices
    mid = n // 2

    A11 = get_submatrix(A, 0, 0, mid)
    A12 = get_submatrix(A, 0, mid, mid)
    A21 = get_submatrix(A, mid, 0, mid)
    A22 = get_submatrix(A, mid, mid, mid)

    B11 = get_submatrix(B, 0, 0, mid)
    B12 = get_submatrix(B, 0, mid, mid)
    B21 = get_submatrix(B, mid, 0, mid)
    B22 = get_submatrix(B, mid, mid, mid)

    # Calcular los 7 productos de Strassen (en lugar de 8)
    M1 = strassen_matrix_multiply(matrix_add(A11, A22), matrix_add(B11, B22))
    M2 = strassen_matrix_multiply(matrix_add(A21, A22), B11)
    M3 = strassen_matrix_multiply(A11, matrix_sub(B12, B22))
    M4 = strassen_matrix_multiply(A22, matrix_sub(B21, B11))
    M5 = strassen_matrix_multiply(matrix_add(A11, A12), B22)
    M6 = strassen_matrix_multiply(matrix_sub(A21, A11), matrix_add(B11, B12))
    M7 = strassen_matrix_multiply(matrix_sub(A12, A22), matrix_add(B21, B22))

    # Calcular las submatrices de C usando los productos M1-M7
    C11 = matrix_add(matrix_sub(matrix_add(M1, M4), M5), M7)
    C12 = matrix_add(M3, M5)
    C21 = matrix_add(M2, M4)
    C22 = matrix_add(matrix_sub(matrix_add(M1, M3), M2), M6)

    # Combinar las submatrices en la matriz resultante
    return combine_submatrices(C11, C12, C21, C22)


def get_submatrix(matrix, start_row, start_col, size):
    """Obtener una submatriz de tamaño size x size"""
    sub = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            sub[i][j] = matrix[start_row + i][start_col + j]
    return sub


def matrix_add(A, B):
    """Suma de dos matrices"""
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]
    return result


def matrix_sub(A, B):
    """Resta de dos matrices"""
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] - B[i][j]
    return result


def combine_submatrices(C11, C12, C21, C22):
    """Combina 4 submatrices en una matriz completa"""
    n = len(C11)
    size = 2 * n
    C = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(n):
        for j in range(n):
            C[i][j] = C11[i][j]
            C[i][j + n] = C12[i][j]
            C[i + n][j] = C21[i][j]
            C[i + n][j + n] = C22[i][j]

    return C


def print_matrix(matrix):
    """Imprimir matriz formateada"""
    for row in matrix:
        print([f"{x:6}" for x in row])