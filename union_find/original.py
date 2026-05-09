def union_find_basic(n):
    parent = [i for i in range(n)]

    def find(x):
        while x != parent[x]:
            x = parent[x]
        return x

    def union(x, y):
        rootX = find(x)
        rootY = find(y)

        if rootX != rootY:
            parent[rootX] = rootY

    return find, union