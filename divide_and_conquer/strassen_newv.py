def add(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]


def sub(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]


def split(M):
    n = len(M)
    mid = n // 2

    A11 = [row[:mid] for row in M[:mid]]
    A12 = [row[mid:] for row in M[:mid]]
    A21 = [row[:mid] for row in M[mid:]]
    A22 = [row[mid:] for row in M[mid:]]

    return A11, A12, A21, A22


def join(C11, C12, C21, C22):
    n = len(C11)

    top = [C11[i] + C12[i] for i in range(n)]
    bottom = [C21[i] + C22[i] for i in range(n)]

    return top + bottom


def strassen(A, B):
    n = len(A)

    # Caso base
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    A11, A12, A21, A22 = split(A)
    B11, B12, B21, B22 = split(B)

    S1 = sub(B12, B22)
    S2 = add(A11, A12)
    S3 = add(A21, A22)
    S4 = sub(B21, B11)
    S5 = add(A11, A22)
    S6 = add(B11, B22)
    S7 = sub(A12, A22)
    S8 = add(B21, B22)
    S9 = sub(A11, A21)
    S10 = add(B11, B12)

    P1 = strassen(A11, S1)
    P2 = strassen(S2, B22)
    P3 = strassen(S3, B11)
    P4 = strassen(A22, S4)
    P5 = strassen(S5, S6)
    P6 = strassen(S7, S8)
    P7 = strassen(S9, S10)

    # Construcción de los bloques resultado
    C11 = add(sub(add(P5, P4), P2), P6)
    C12 = add(P1, P2)
    C21 = add(P3, P4)
    C22 = sub(sub(add(P5, P1), P3), P7)

    return join(C11, C12, C21, C22)