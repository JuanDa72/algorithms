def sum_mat(array1, array2):
    n=len(array1)
    sum=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            sum[i][j]=array1[i][j]+array2[i][j]


def join(C11, C12, C21, C22):
    n = len(C11)

    top = [C11[i] + C12[i] for i in range(n)]
    bottom = [C21[i] + C22[i] for i in range(n)]

    return top + bottom

def split(M):
    n = len(M)
    mid = n // 2

    A11 = [row[:mid] for row in M[:mid]]
    A12 = [row[mid:] for row in M[:mid]]
    A21 = [row[:mid] for row in M[mid:]]
    A22 = [row[mid:] for row in M[mid:]]

    return [A11, A12, A21, A22]

def div_sum(array1, array2):
    n=len(array1)

    if n == 1:
        return [[array1[0][0] + array2[0][0]]]

    else:
        partes_a1 = split(array1)
        partes_a2 = split(array2)

        for i in range(len(partes_a1)):
            vs=[]
            value=div_sum(partes_a1[i], partes_a2[i])
            vs.append(value)

        for 
        



    
