def parent(i):
    return (i-1)//2

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def max_heapify(A, i, n):
    l=left(i)
    r=right(i)
    largest = i

    if l<=n-1 and A[l]>A[i]:
        largest=l

    if r<=n-1 and A[r]>A[largest]:
        largest=r

    if i!=largest:
        A[i], A[largest]=A[largest], A[i]
        max_heapify(A, largest, n)

def building_max_heap(A, n):
    limit=(n-1)//2
    for i in range(limit, -1, -1):
        max_heapify(A,i,n)

def heap_sort(A, n):
    building_max_heap(A, n)
    for i in range(n-1, 0, -1):
        A[0], A[i]=A[i], A[0]
        n-=1
        max_heapify(A,0,n)

array=[1,2,4,5,3,5,3,2,5,3,1953,494]
heap_sort(array, len(array))
print(array)
