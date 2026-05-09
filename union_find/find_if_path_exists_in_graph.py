def validPath(n: int, edges: list[list[int]], source: int, destination: int) -> bool:

    def union_find_optimized(n):
        parent = [i for i in range(n)]
        rank = [0] * n

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return

            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootX] = rootY
                rank[rootY] += 1

        return find, union

    find, union= union_find_optimized(n)

    for l in edges:
        if l[0]==source:
            union(l[1], l[0])

        elif l[1]==source:
            union(l[0], l[1])

    if find(destination)==source:
        return True

    for l in edges:
        if l[0]!=source and l[1]!=source:

            if find(l[0])==source:
                union(l[1], l[0])

            elif find(l[1])==source:
                union(l[0], l[1])

    return True if find(destination)==source else False


print(validPath(3,[[0,1],[1,2],[2,0]], 0, 2))


