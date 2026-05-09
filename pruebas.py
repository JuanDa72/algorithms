def matrix_multiply_dc(A, B):
    """
    Multiplicación de matrices usando Divide y Vencerás
    Asume matrices cuadradas n x n donde n es potencia de 2
    """
    n = len(A)

    # Caso base: matriz 1x1
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Dividir matrices en 4 submatrices cada una
    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    print(A11)



def add_matrices(A, B):
    """Suma de dos matrices"""
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]


#matrix_multiply_dc([[1,2],[4,5]],[[1,2,3],[4,5,6],[7,8,9]])
print(add_matrices([[1,2],[2,4]],[[4,5],[5,6]]))
