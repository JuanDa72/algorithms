def countNegatives(grid: list[list[int]]) -> int:
    negatives: int = 0
    for i in range(len(grid)):
        row = grid[i]
        left = 0
        right = len(row) - 1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if row[mid] < 0:
                ans = mid
                right = mid - 1

            else:
                left = mid + 1

        negatives += len(row) - ans

    return negatives


print(countNegatives([[3,2],[1,0]]))