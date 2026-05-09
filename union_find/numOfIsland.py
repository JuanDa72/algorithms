def numIslands(self, grid: list[list[str]]) -> int:
    if not grid:
        return 0

    m,n =len(grid), len(grid[0])

    parent=[i for i in range(m*n)]
    rank=[0]*(m*n)

    def find(x):
        if parent[x]!=x:
            parent[x]=find(parent[x])

        return parent[x]

    def union(x,y):
        rootX=find(x)
        rootY=find(y)

        if rootX==rootY:
            return 0

        if rank[rootX]>rank[rootY]:
            parent[rootY]=rootX

        elif rank[rootX]<rank[rootY]:
            parent[rootX]=rootY

        else:
            parent[rootY]=rootX
            rank[rootX]+=1

        return 1

    count=0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                count += 1


    for i in range(m):
        for j in range(n):
            if grid[i][j]=="1":
                idx=i*n +j

                for dx, dy in [(1,0), (0,1)]:
                    ni, nj=i +dx, j +dy

                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "1":
                        count -= union(idx, ni * n + nj)

    return count