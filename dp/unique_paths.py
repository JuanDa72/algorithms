def uniquePaths(m: int, n: int) -> int:
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

    return dp[m - 1][n - 1]



print(uniquePaths(1,1))