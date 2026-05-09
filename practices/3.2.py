def insertion_sort(a):
    n=len(a)
    comparations=0
    for i in range(1,n):
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            comparations+=1
            a[j+1]=a[j]
            j=j-1

        a[j+1]=key
        comparations+=1

    return a,comparations

n=int(input())
for i in range(n):
    array=list(map(int, input().split()))
    sorted,c=insertion_sort(array)
    size=len(array)
    if c==size-1:
        print(f"{c} Best")

    elif c==((size*(size+1))/2)-1:
        print(f"{c} Worst")

    else:
        print(f"{c} Average")
