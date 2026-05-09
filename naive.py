def matrix_multiply_naive(A, B):
    """
    Multiplicación naive de matrices A × B

    Args:
        A: matriz m × n (lista de listas)
        B: matriz n × p (lista de listas)

    Returns:
        C: matriz m × p resultante
    """
    m = len(A)
    n = len(A[0])
    p = len(B[0])

    # Verificar dimensiones compatibles
    if len(B) != n:
        raise ValueError("Dimensiones incompatibles: A.columns != B.rows")

    # Crear matriz resultado llena de ceros
    C = [[0 for _ in range(p)] for _ in range(m)]

    # Algoritmo naive
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


# Función para imprimir matrices bonito
def print_matrix(matrix):
    for row in matrix:
        print([f"{x:3}" for x in row])