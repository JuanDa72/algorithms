def solve(board: list[list[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    n = len(board)
    m = len(board[0])

    parent=[i for i in range(m*n +1)]
    rank=[0]*(m*n +1)

    dummy=m*n

    def find(x):
        if parent[x]!=x:
            parent[x]=find(parent[x])

        return parent[x]

    def union(x,y):
        root_x=find(x)
        root_y=find(y)

        if root_x==root_y:
            return


        if rank[root_x]>rank[root_y]:
            parent[root_y]=root_x

        elif rank[root_x]<rank[root_x]:
            parent[root_x]=root_y

        else:
            parent[root_y]=root_x
            rank[root_x]+=1

    for i in range(m):
        for j in range(n):
            if board[i][j]=="O":
                idx=i*n +j

                if i==0 or i==m-1 or j==0 or j==n-1:
                    union(idx, dummy)

                dirs=[(1,0), (-1,0), (0,1), (0,-1)]
                for dx, dy in dirs:
                    ni, nj=i+dx, j+dy

                    if 0<=ni<m and 0<=nj <n and board[ni][nj]=="O":
                        union(idx, ni*n + nj)

    for i in range(m):
        for j in range(n):
            if board[i][j]=="O":
                idx=i*n+j

                if find(idx) != find(dummy):
                    board[i][j]="X"






print(solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
