def minimumTotal(triangle: list[list[int]]) -> int:
    n=len(triangle[-1])
    dp=[[0]*(i+1) for i in range(n)]

    for i in range(n):
        current = triangle[i]
        for j in range(len(current)):
            if i == 0:
                dp[i][j] = current[0]

            elif i == 1:
                dp[i][j] = dp[i-1][0] + triangle[i][j]

            else:
                if j==0:
                    dp[i][j]=dp[i-1][0]+ triangle[i][j]

                elif j==len(current)-1:
                    dp[i][j]=dp[i-1][j-1]+triangle[i][j]

                else:
                    dp[i][j]=min(dp[i-1][j-1], dp[i-1][j])+triangle[i][j]


    return min(dp[n-1])


print(minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))