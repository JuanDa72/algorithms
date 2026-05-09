def isInterleave(s1: str, s2: str, s3: str) -> bool:
    m, n = len(s1), len(s2)

    if m + n < len(s3):
        return False

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    dp[0][0] = True

    for i in range(m + 1):

        for j in range(n + 1):

            if i + j - 1 > len(s3)-1:
                break

            if i > 0 and s3[i + j - 1] == s1[i - 1] and dp[i - 1][j]:
                dp[i][j] = True

            if j > 0 and s3[i + j - 1] == s2[j - 1] and dp[i][j - 1]:
                dp[i][j] = True

    return dp[m][n]


print(isInterleave("a", "b", "a"))