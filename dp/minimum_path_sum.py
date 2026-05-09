def minPathSum(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]

            else:
                current = []
                if i - 1 >= 0:
                    current.append(dp[i - 1][j])

                elif j - 1 >= 0:
                    current.append(dp[i][j - 1])

                dp[i][j] = min(current) + grid[i][j]

    return dp[m - 1][n - 1]


print(minPathSum([[1,2],[1,1]]))