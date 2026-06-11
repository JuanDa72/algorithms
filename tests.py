def split(M):
    n = len(M)
    mid = n // 2

    A11 = [row[:mid] for row in M[:mid]]
    A12 = [row[mid:] for row in M[:mid]]
    A21 = [row[:mid] for row in M[mid:]]
    A22 = [row[mid:] for row in M[mid:]]

    return [A11, A12, A21, A22]


m=[[0,4,3,3],[-4,5,-2,-2], [-5,-5,2,-1], [-1,-3,5,-1]]

split(m)