def longestConsecutive(nums: list[int]) -> int:
    if not nums:
        return 0

    nums= list(set(nums))
    n = len(nums)

    parent = [i for i in range(n)]
    size = [1] * n

    num_to_index = {num: i for i, num in enumerate(nums)}

    def find(x):
        if parent[x]!=x:
            parent[x]=find(parent[x])

        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)

        if root_x == root_y:
            return

        if size[root_x] > size[root_y]:
            parent[root_y] = root_x
            size[root_x] += size[root_y]

        else:
            parent[root_x] = root_y
            size[root_y] += size[root_x]

    for num in nums:
        if num + 1 in num_to_index:
            union(num_to_index[num], num_to_index[num + 1])

    return max(size)


print(longestConsecutive([100,4,200,1,3,2]))
