def maximalSquare(matrix: list[list[str]]) -> int:
    r = len(matrix)
    c = len(matrix[0])
    maximum = 0

    dp = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if i == 0 or j == 0:
                if matrix[i][j] == 1:
                    dp[i][j] = 1

            else:
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

            if dp[i][j] > maximum:
                maximum = dp[i][j]

    return maximum ** 2


print(maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))