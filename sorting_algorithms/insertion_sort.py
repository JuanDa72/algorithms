def insertion_sort(a):
    n=len(a)
    for i in range(1,n):
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j=j-1

        a[j+1]=key

    return a


print(insertion_sort([24,42,5,3,2,6,4,32,4]))
