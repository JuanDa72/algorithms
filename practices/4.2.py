def merge(A, p, q, r):
    """
    :param A: Array
    :param p: Index of the first position of the array
    :param q: Index of the last position of first part-array
    :param r: Index of the last position of the second array
    """

    L=A[p:q+1]
    R=A[q+1:r+1]
    i,j=0,0
    k=p

    while i<len(L) and j<len(R):
        if L[i]>=R[j]:
            A[k]=L[i]
            i+=1

        else:
            A[k]=R[j]
            j+=1

        k+=1

    while i<len(L):
        A[k]=L[i]
        i+=1
        k+=1

    while j<len(R):
        A[k] = R[j]
        j += 1
        k += 1
    
    #print("Impresion de merge:")
    print(" ".join(map(str, A[p:r+1])))

    

def merge_sort(A, p, r):
    """
    :param A: Array
    :param p: Index of first position of array A
    :param r: Index of the final position of array A
    """
    #print("Impresion de merge_sort:")
    print(" ".join(map(str, A[p:r+1])))
    if p>=r:
        #Zero or one element
        return

    q=(p+r)//2
    merge_sort(A, q+1, r)
    merge_sort(A, p, q)
    merge(A, p, q, r)

#array=[14, 6, 10, 11, 2]
#merge_sort(array, 0, len(array)-1)
#print(array)


array=list(map(int, input().split()))
merge_sort(array, 0, len(array)-1)
#print(array)
