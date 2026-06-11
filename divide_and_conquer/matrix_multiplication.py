def split(M):
    n = len(M)
    mid = n // 2

    A11 = [row[:mid] for row in M[:mid]]
    A12 = [row[mid:] for row in M[:mid]]
    A21 = [row[:mid] for row in M[mid:]]
    A22 = [row[mid:] for row in M[mid:]]

    return [A11, A12, A21, A22]

def join(C11, C12, C21, C22):
    n = len(C11)

    top = [C11[i] + C12[i] for i in range(n)]
    bottom = [C21[i] + C22[i] for i in range(n)]

    return top + bottom

def div_sum(array1, array2):
    n=len(array1)

    if n == 1:
        return [[array1[0][0] + array2[0][0]]]

    else:
        partes_a1 = split(array1)
        partes_a2 = split(array2)

        C11 = div_sum(partes_a1[0], partes_a2[0])
        C12 = div_sum(partes_a1[1], partes_a2[1])
        C21 = div_sum(partes_a1[2], partes_a2[2])
        C22 = div_sum(partes_a1[3], partes_a2[3])

        result=join(C11,C12,C21,C22)
        return result


def mul_dac(M1, M2):
    if len(M1)==1:
        return [[M1[0][0]*M2[0][0]]]

    else:
        A11, A12, A21, A22=split(M1)
        B11, B12, B21, B22=split(M2)

        C11=div_sum(mul_dac(A11, B11), mul_dac(A12, B21))
        C12=div_sum(mul_dac(A11, B12), mul_dac(A12, B22))
        C21=div_sum(mul_dac(A21, B11), mul_dac(A22, B21))
        C22=div_sum(mul_dac(A21, B12), mul_dac(A22, B22))

        return join(C11, C12, C21, C22)

f=list(map(int, input().split(" ")))
n=len(f)
matriz_a=[f]
matriz_b=[]
for i in range(1, n):
    matriz_a.append(list(map(int, input().split(" "))))

for j in range(0,n):
    matriz_b.append(list(map(int, input().split(" "))))

print(mul_dac(matriz_a, matriz_b))