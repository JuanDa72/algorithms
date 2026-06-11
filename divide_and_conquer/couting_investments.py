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
    investment=0

    while i<len(L) and j<len(R):
        if L[i]<=R[j]:
            A[k]=L[i]
            i+=1

        else:
            A[k]=R[j]
            j+=1
            investment+=len(L)-i

        k+=1

    while i<len(L):
        A[k]=L[i]
        i+=1
        k+=1

    while j<len(R):
        A[k] = R[j]
        j += 1
        k += 1

    return investment

def merge_sort(A, p, r):
    inv=0
    """
    :param A: Array
    :param p: Index of first position of array A
    :param r: Index of the final position of array A
    """
    if p>=r:
        #Zero or one element
        return 0

    q=(p+r)//2
    inv+=merge_sort(A, p, q)
    inv+=merge_sort(A, q+1, r)
    inv+=merge(A, p, q, r)
    return inv

array=[3,5,2,4,6,4]
print(merge_sort(array, 0, len(array)-1))
#print(array)
