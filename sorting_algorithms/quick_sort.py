def partition(A,p,r):
    "The pivot is the last element"
    x=A[r]
    i=p-1
    for j in range(p, r):
        if A[j]<=x:
            i+=1
            A[i], A[j]=A[j], A[i]

    A[i+1], A[r]=A[r], A[i+1]
    "Return the index of pivot which is already in the correct position"
    return i+1


def quick_sort(A, p, r):
    """
    :param A: Array
    :param p: first index
    :param r: last index
    """
    if p<r:
        q=partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

array=[1,4743,6,3,54,4,77,4,2,5,7,88,8]
quick_sort(array,0,len(array)-1)
print(array)