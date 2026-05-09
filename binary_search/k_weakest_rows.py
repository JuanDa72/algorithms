def kWeakestRows(mat: list[list[int]], k: int) -> list[int]:
    l:list=[]
    for i in range(len(mat)):
        row:list[int]=mat[i]
        left=0
        right=len(row)-1
        while left<=right:
            mid=(left+right)//2
            if row[mid]==1:
                left=mid+1

            else:
                right=mid-1

        l.append((left, i))

    l.sort()

    return [index for _,index in l[:k]]


print(kWeakestRows([[1,0],[1,0],[1,0],[1,1]], 4))